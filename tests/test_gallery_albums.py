import pytest
import allure
from pages.gallery_page import GalleryPage
from pages.gallery_album_page import GalleryAlbumPage

@allure.title("Подсчёт изображений в каждом альбоме галереи")
@allure.severity(allure.severity_level.NORMAL)
def test_count_images_per_album(driver):
    driver.get("https://modultest1.framer.website/")

    gallery = GalleryPage(driver)
    gallery.go_to_gallery()

    albums = gallery.get_album_elements()
    assert len(albums) >= 1, "Альбомы не найдены"

    album_infos = []

    for i in range(len(albums)):
        gallery = GalleryPage(driver)
        gallery.scroll_to_album_by_index(i)

        albums = gallery.get_album_elements()
        album_name = albums[i].text or f"Альбом #{i+1}"
        albums[i].click()

        album = GalleryAlbumPage(driver)
        image_count = album.get_images_count()

        album_infos.append((album_name.strip(), image_count))
        album.go_back_to_gallery()

    for name, count in album_infos:
        print(f"{name}: {count} изображений")
        allure.attach(body=f"{name}: {count} изображений",
                      name=f"Альбом: {name}",
                      attachment_type=allure.attachment_type.TEXT)
