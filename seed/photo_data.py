from main.models import Photo

Photo.objects.all().delete()

Photo.objects.create(
    image="img/photos/bedroom.avif",
    description="Bedroom",
    track=1,
    position=1,
)

Photo.objects.create(
    image="img/photos/bible.avif",
    description="Bible",
    track=1,
    position=2,
)

Photo.objects.create(
    image="img/photos/bus-stop.avif",
    description="Bus stop",
    track=1,
    position=3,
)

Photo.objects.create(
    image="img/photos/cafe.avif",
    description="Cafe",
    track=1,
    position=4,
)

Photo.objects.create(
    image="img/photos/city-road.avif",
    description="City road",
    track=2,
    position=1,
)

Photo.objects.create(
    image="img/photos/dark-road.avif",
    description="Dark road",
    track=2,
    position=2,
)

Photo.objects.create(
    image="img/photos/forest.avif",
    description="Forest",
    track=2,
    position=3,
)

Photo.objects.create(
    image="img/photos/orchid.avif",
    description="Orchid",
    track=2,
    position=4,
)

Photo.objects.create(
    image="img/photos/parking-lot.avif",
    description="Parking lot",
    track=3,
    position=1,
)

Photo.objects.create(
    image="img/photos/ruby.avif",
    description="Ruby",
    track=3,
    position=2,
)

Photo.objects.create(
    image="img/photos/station.avif",
    description="Station",
    track=3,
    position=3,
)

Photo.objects.create(
    image="img/photos/ugm.avif",
    description="UGM",
    track=3,
    position=4,
)

