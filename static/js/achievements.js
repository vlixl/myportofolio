/* Tutorial 7: Achievements backed by DRF while retaining the existing UI. */
(function () {
    const config = window.ACHIEVEMENTS_CONFIG;
    const loadingState = document.getElementById('achievement-loading');
    const errorState = document.getElementById('achievement-error');
    const emptyState = document.getElementById('achievement-empty');
    const listContainer = document.getElementById('achievement-items');
    const searchForm = document.getElementById('achievement-search-form');
    const searchInput = document.getElementById('search-input');
    const achievementForm = document.getElementById('achievement-add-form');
    let abortController;
    let searchDebounceTimer;

    function displayState({ showLoading = false, showError = false,
                            showEmpty = false, showList = false }) {
        loadingState.classList.toggle('hide', !showLoading);
        errorState.classList.toggle('hide', !showError);
        emptyState.classList.toggle('hide', !showEmpty);
        listContainer.classList.toggle('hide', !showList);
    }

    function achievementUrl(pattern, id) {
        return pattern.replace(config.dummyId, id);
    }

    function buildAchievementElement(a) {
        const editUrl = config.editUrlTemplate.replace(config.dummyId, a.id);
        const starTitle = a.star_count > 0
            ? `Dibintangi oleh ${escapeHtml(a.starred_by_names)}`
            : 'Jadilah yang pertama memberi star';
        const editHtml = a.can_change
            ? `<a href="${escapeHtml(editUrl)}" class="edit-achievement">Edit</a>` : '';
        const deleteHtml = a.can_delete
            ? `<button type="button" class="delete-achievement" data-action="delete"
                data-id="${escapeHtml(a.id)}">Delete</button>` : '';
        const starHtml = config.isAuthenticated
            ? `<button type="button" data-action="star" data-id="${escapeHtml(a.id)}"
                    class="button-star${a.is_starred ? ' is-starred' : ''}" title="${starTitle}">
                    <span class="material-symbols-outlined star-icon">star</span>
                    <span class="star-count">${escapeHtml(a.star_count)}</span>
                </button>`
            : `<a href="${escapeHtml(config.loginUrl)}" class="button-star"
                    title="Login to star"><span class="material-symbols-outlined star-icon">star</span>
                    <span class="star-count">${escapeHtml(a.star_count)}</span></a>`;
        const article = document.createElement('article');
        article.className = 'achievement-row';
        article.innerHTML = `
            <div class="star-form">${starHtml}</div>
            <h2 class="award-result"><span>${escapeHtml(a.award)}</span> ${escapeHtml(a.award_label)}</h2>
            <div class="award-detail">
                <p>${escapeHtml(a.category)} · ${escapeHtml(a.month_display)} ${escapeHtml(a.year)}</p>
                <h3>${escapeHtml(a.event)}</h3>
                <p>${escapeHtml(a.organization)}</p>
                <p>${escapeHtml(a.description)}</p>
                <div class="achievement-form">${editHtml}${deleteHtml}</div>
            </div>`;
        return article;
    }

    async function fetchAchievements(searchQuery = '') {
        if (abortController) abortController.abort();
        abortController = new AbortController();
        try {
            displayState({ showLoading: true });
            const url = new URL(config.listEndpoint, window.location.origin);
            if (searchQuery) url.searchParams.set('title', searchQuery);
            const response = await fetch(url, {
                headers: { Accept: 'application/json' },
                signal: abortController.signal,
            });
            if (!response.ok) throw new Error(`HTTP ${response.status}`);
            const data = await response.json();
            listContainer.replaceChildren(...data.map(buildAchievementElement));
            displayState({ showEmpty: data.length === 0, showList: data.length > 0 });
        } catch (error) {
            if (error.name === 'AbortError') return;
            console.error(error);
            displayState({ showError: true });
        }
    }

    function errorMessage(data, code) {
        const messages = Object.values(data).flat().filter(value => typeof value === 'string');
        return messages.join(' ') || `Request failed (HTTP ${code}).`;
    }

    async function writeAchievement(url, method, payload) {
        const response = await fetch(url, {
            method,
            headers: {
                Accept: 'application/json',
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken') || '',
            },
            body: payload === undefined ? undefined : JSON.stringify(payload),
        });
        if (response.status === 204) return null;
        const data = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error(errorMessage(data, response.status));
        return data;
    }

    async function addAchievement(event) {
        event.preventDefault();
        const button = achievementForm.querySelector('button[type="submit"]');
        button.disabled = true;
        try {
            const fields = new FormData(achievementForm);
            const payload = Object.fromEntries([
                'award', 'award_label', 'category', 'month', 'year',
                'event', 'organization', 'description',
            ].map(name => [name, fields.get(name)]));
            await writeAchievement(config.listEndpoint, 'POST', payload);
            achievementForm.reset();
            document.getElementById('add-achievement-modal').hidePopover();
            showToast('Berhasil', 'Achievement ditambahkan!', 'success');
            await fetchAchievements(searchInput.value.trim());
        } catch (error) {
            showToast('Gagal menambahkan achievement', error.message, 'error');
        } finally {
            button.disabled = false;
        }
    }
    if (achievementForm) achievementForm.addEventListener('submit', addAchievement);

    listContainer.addEventListener('click', async function (event) {
        const button = event.target.closest('button[data-action]');
        if (!button || button.disabled) return;
        const action = button.dataset.action;
        if (action === 'delete' && !window.confirm('Yakin ingin menghapus achievement ini?')) return;
        button.disabled = true;
        try {
            const pattern = action === 'star' ? config.starUrlTemplate : config.detailUrlTemplate;
            await writeAchievement(achievementUrl(pattern, button.dataset.id),
                action === 'star' ? 'POST' : 'DELETE');
            showToast('Berhasil', action === 'star' ? 'Star diperbarui.' : 'Achievement dihapus.', 'success');
            await fetchAchievements(searchInput.value.trim());
        } catch (error) {
            showToast('Request gagal', error.message, 'error');
        } finally {
            button.disabled = false;
        }
    });

    searchInput.addEventListener('input', function () {
        clearTimeout(searchDebounceTimer);
        searchDebounceTimer = setTimeout(() => fetchAchievements(searchInput.value.trim()), 300);
    });
    searchForm.addEventListener('submit', function (event) {
        event.preventDefault();
        clearTimeout(searchDebounceTimer);
        fetchAchievements(searchInput.value.trim());
    });
    fetchAchievements(searchInput.value.trim());
})();
