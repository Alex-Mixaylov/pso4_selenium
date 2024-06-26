from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def init_browser():
    # Инициализация браузера
    browser = webdriver.Chrome()
    return browser


def search_wikipedia(browser, query):
    # Поиск статьи на Википедии
    url_wiki = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    browser.get(url_wiki)
    assert "Википедия" in browser.title
    search_box = browser.find_element(By.ID, "searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    #Поиск на Википедии может иногда перенаправлять на страницу результатов поиска,
    # вместо того чтобы сразу открывать нужную статью.
    # Для решения этой проблемы можно сделать следующее:

    # Проверка, есть ли в URL подстрока "search"
    if "search" in browser.current_url:
        # Клик на первой ссылке в результатах поиска
        # Этот селектор в совокупности выбирает все ссылки внутри элементов <li>,
        # которые находятся внутри списка <ul> с классом mw-search-results.
        first_result = browser.find_element(By.CSS_SELECTOR, "ul.mw-search-results li a") #Селектор ul.mw-search-results li a
        first_result.click()
        time.sleep(2)


def list_paragraphs(browser):
    # Листаем параграфы текущей статьи
    paragrafs = browser.find_elements(By.TAG_NAME, "p")
    for paragraf in paragrafs:
        print(paragraf.text)
        user_input = input("Нажмите ВВОД для продолжения или введите ВЫХОД для выхода из режима просмотра параграфов ")
        if user_input.lower() == 'выход':
            break


def list_related_links(browser):
    # Переход на одну из связанных страниц
    links = browser.find_elements(By.CSS_SELECTOR, "a[title]")
    related_links = []
    for link in links:
        href = link.get_attribute("href")
        if 'wiki' in href:
            related_links.append((link.text, href))

    for i, (text, href) in enumerate(related_links):
        print(f"{i + 1}: {text} - {href}")

    return related_links


def main():
    browser = init_browser()

    try:
        initial_query = input("Введите первоначальный запрос: ")
        search_wikipedia(browser, initial_query)

        while True:
            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")
            choice = input("Введите номер действия (1, 2, 3): ")

            if choice == '1':
                list_paragraphs(browser)
            elif choice == '2':
                related_links = list_related_links(browser)
                if not related_links:
                    print("Связанных страниц не найдено.")
                    continue

                link_choice = input("Введите номер связанной страницы для перехода или 'НАЗАД' для возврата: ")
                if link_choice.lower() == 'назад':
                    continue

                try:
                    link_index = int(link_choice) - 1
                    if 0 <= link_index < len(related_links):
                        browser.get(related_links[link_index][1])
                        time.sleep(2)
                    else:
                        print("Неверный выбор.")
                except ValueError:
                    print("Пожалуйста, введите корректный номер.")
            elif choice == '3':
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор, попробуйте снова.")
    finally:
        browser.quit()


if __name__ == "__main__":
    main()
