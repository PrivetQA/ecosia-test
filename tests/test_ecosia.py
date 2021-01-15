from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss, s


def test_search():
    browser.open('https://www.ecosia.org/')

    query_field = s('[name=q]')
    query_field.type('yashaka selene').press_enter()
    ss('.result').first.click()

    ss('[href="/yashaka/selene"]').should(have.size(3))
