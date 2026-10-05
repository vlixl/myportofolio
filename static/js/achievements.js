
/*
 * Achievements: AJAX list, debounced search, dan modal tambah data.
 * Membutuhkan: utils.js (escapeHtml, getCookie), toast.js (showToast),
 * dan objek global ACHIEVEMENTS_CONFIG yang didefinisikan di index.html.
 */
(function () {
    const config = window.ACHIEVEMENTS_CONFIG;
    const SEARCH_DEBOUNCE_DELAY = 300;

    // Elemen DOM
    const loadingState = document.getElementById('achievement-loading');
    const errorState = document.getElementById('achievement-error');
    const emptyState = document.getElementById('achievement-empty');
    const listContainer = document.getElementById('achievement-items');
    const searchForm = document.getElementById('achievement-search-form');
    const searchInput = document.getElementById('search-input');
    const achievementForm = document.getElementById('achievement-add-form'); // null jika tanpa izin

    let abortController;
    let searchDebounceTimer;

    // Menampilkan hanya satu state pada satu waktu
    function displayState({ showLoading = false, showError = false, showEmpty = false, showList = false }) {
        loadingState.classList.toggle('hide', !showLoading);
        errorState.classList.toggle('hide', !showError);
        emptyState.classList.toggle('hide', !showEmpty);
        listContainer.classList.toggle('hide', !showList);
    }

    // Membangun satu baris achievement; semua teks dari server di-escape
    function buildAchievementElement(item) {
        const a = item.fields;
        const id = item.pk;

        const editUrl = config.editUrlTemplate.replace(config.dummyId, id);
        const deleteUrl = config.deleteUrlTemplate.replace(config.dummyId, id);
        const starUrl = config.starUrlTemplate.replace(config.dummyId, id);
        const csrfToken = escapeHtml(getCookie('csrftoken') || '');

        const starTitle = a.star_count > 0
            ? `Dibintangi oleh ${escapeHtml(a.starred_by_names)}`
            : 'Jadilah yang pertama memberi star';

        const editHtml = a.can_change
            ? `<a href="${escapeHtml(editUrl)}" class="edit-achievement">Edit</a>`
            : '';
        const deleteHtml = a.can_delete
            ? `<form action="${escapeHtml(deleteUrl)}" method="POST">
                    <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                    <button type="submit" class="delete-achievement"
                            onclick="return confirm('Yakin ingin menghapus achievement ini?');">Delete</button>
               </form>`
            : '';

        const article = document.createElement('article');
        article.className = 'achievement-row';
        article.innerHTML = `
            <form method="post" action="${escapeHtml(starUrl)}" class="star-form">
                <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                <button type="submit"
                        class="button-star${a.is_starred ? ' is-starred' : ''}"
                        title="${starTitle}">
                    <span class="material-symbols-outlined star-icon">star</span>
                    <span class="star-count">${escapeHtml(a.star_count)}</span>
                </button>
            </form>
            <h2 class="award-result">
                <span>${escapeHtml(a.award)}</span>
                ${escapeHtml(a.award_label)}
            </h2>
            <div class="award-detail">
                <p>${escapeHtml(a.category)} · ${escapeHtml(a.month_display)} ${escapeHtml(a.year)}</p>
                <h3>${escapeHtml(a.event)}</h3>
                <p>${escapeHtml(a.organization)}</p>
                <p>${escapeHtml(a.description)}</p>
                <div class="achievement-form">
                    ${editHtml}
                    ${deleteHtml}
                </div>
            </div>
        `;
        return article;
    }

    // Mengambil data achievement dari endpoint JSON
    async function fetchAchievements(searchQuery = '') {
        if (abortController) abortController.abort();
        abortController = new AbortController();

        try {
            displayState({ showLoading: true });

            const url = searchQuery
                ? `${config.listEndpoint}?title=${encodeURIComponent(searchQuery)}`
                : config.listEndpoint;

            const response = await fetch(url, {
                headers: { 'Accept': 'application/json' },
                signal: abortController.signal,
            });
            if (!response.ok) throw new Error(`Failed to fetch data (status ${response.status})`);

            const data = await response.json();

            if (data.length === 0) {
                displayState({ showEmpty: true });
                return;
            }

            listContainer.innerHTML = '';
            data.forEach(item => listContainer.appendChild(buildAchievementElement(item)));
            displayState({ showList: true });
        } catch (error) {
            if (error.name === 'AbortError') return;
            console.error('Error loading achievements:', error);
            displayState({ showError: true });
        }
    }

    // Search dengan debouncing: request hanya dikirim setelah pengguna berhenti mengetik
    searchInput.addEventListener('input', function () {
        clearTimeout(searchDebounceTimer);
        searchDebounceTimer = setTimeout(
            () => fetchAchievements(searchInput.value.trim()),
            SEARCH_DEBOUNCE_DELAY
        );
    });

    searchForm.addEventListener('submit', function (event) {
        event.preventDefault();
        clearTimeout(searchDebounceTimer);
        fetchAchievements(searchInput.value.trim());
    });

    // Mengirim form tambah achievement
    async function addAchievement(event) {
        event.preventDefault();

        const submitButton = achievementForm.querySelector('button[type="submit"]');
        submitButton.disabled = true;

        try {
            const response = await fetch(config.createEndpoint, {
                method: 'POST',
                headers: { 'X-CSRFToken': getCookie('csrftoken') },
                body: new FormData(achievementForm),
            });
            const result = await response.json().catch(() => ({}));

            if (response.ok) {
                achievementForm.reset();
                document.getElementById('add-achievement-modal').hidePopover();
                showToast('Berhasil', 'Achievement baru berhasil ditambahkan!', 'success');
                fetchAchievements(searchInput.value.trim());
            } else {
                const errorMessages = result.errors
                    ? Object.values(result.errors).flat().map(error => error.message)
                    : [result.message || `Terjadi kesalahan (status ${response.status}).`];
                showToast('Gagal menambahkan achievement', errorMessages.join(' '), 'error');
            }
        } catch (error) {
            console.error('Error adding achievement:', error);
            showToast('Gagal menambahkan achievement', 'Tidak dapat terhubung ke server. Silakan coba lagi.', 'error');
        } finally {
            submitButton.disabled = false;
        }
    }

    // Modal hanya dirender untuk pengguna berizin, jadi elemennya bisa null
    if (achievementForm) {
        achievementForm.addEventListener('submit', addAchievement);
    }

    fetchAchievements(searchInput.value.trim());
})();
