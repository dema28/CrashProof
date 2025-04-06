import allure
from pages.gallery_page import GalleryPage
from pages.gallery_album_page import GalleryAlbumPage
from pages.main_page import MainPage

@allure.title("Image count in each gallery album")
@allure.severity(allure.severity_level.NORMAL)
def test_count_images_per_album(driver):
    with allure.step("Opening the website"):
        driver.get(MainPage.URL)

    gallery = GalleryPage(driver)

    with allure.step("Navigating to gallery page"):
        gallery.go_to_gallery()

    with allure.step("Getting list of albums"):
        albums = gallery.get_album_elements()
        assert len(albums) >= 1, "No albums found"

    album_infos = []

    for i in range(len(albums)):
        with allure.step(f"Album #{i+1}: scrolling and opening"):
            gallery = GalleryPage(driver)
            gallery.scroll_to_album_by_index(i)

            albums = gallery.get_album_elements()
            album_name = albums[i].text or f"Album #{i+1}"
            albums[i].click()

        with allure.step(f"Album '{album_name.strip()}': counting images"):
            album = GalleryAlbumPage(driver)
            image_count = album.get_images_count()
            album_infos.append((album_name.strip(), image_count))

        with allure.step("Returning to album list"):
            album.go_back_to_gallery()

    for name, count in album_infos:
        print(f"{name}: {count} images")
        allure.attach(body=f"{name}: {count} images",
                      name=f"Album: {name}",
                      attachment_type=allure.attachment_type.TEXT)
