import os.path
from selene import browser, be, command, by, have


def test_fill_and_send_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Firstname')
    browser.element('#lastName').should(be.blank).type('Lastname')
    browser.element('#userEmail').should(be.blank).type('random@gmail.com')
    browser.element('[for="gender-radio-3"]').click()
    browser.element("#userNumber").should(be.blank).type('0123456789')

    browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    browser.element('//select[@class="react-datepicker__month-select"]').click()
    browser.element('//select[@class="react-datepicker__month-select"]').click().element('option[value="8"]').click()
    browser.element('//select[@class="react-datepicker__year-select"]').click().element('option[value="1999"]').click()
    browser.element('.react-datepicker__day--025').click()

    browser.element('#subjectsInput').should(be.blank).type('Arts').press_enter()
    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('images/image.png'))
    browser.element("#currentAddress").should(be.blank).type("Random street")
    browser.element('#state').click().element(by.text('NCR')).click()
    browser.element('#city').click().element(by.text('Delhi')).click()
    browser.element('#submit').click()

    browser.element('.modal-header').should(have.text("Thanks for submitting the form"))
    browser.element("tbody tr:nth-child(1) td:nth-child(2)").should(have.text('Firstname Lastname'))
    browser.element("tbody tr:nth-child(2) td:nth-child(2)").should(have.text('random@gmail.com'))
    browser.element("tbody tr:nth-child(3) td:nth-child(2)").should(have.text('Other'))
    browser.element("tbody tr:nth-child(4) td:nth-child(2)").should(have.text('0123456789'))
    browser.element("tbody tr:nth-child(5) td:nth-child(2)").should(have.text('25 September,1999'))
    browser.element("tbody tr:nth-child(6) td:nth-child(2)").should(have.text('Arts'))
    browser.element("tbody tr:nth-child(7) td:nth-child(2)").should(have.text('Reading'))
    browser.element("tbody tr:nth-child(8) td:nth-child(2)").should(have.text('image.png'))
    browser.element("tbody tr:nth-child(9) td:nth-child(2)").should(have.text('Random street'))
    browser.element("tbody tr:nth-child(10) td:nth-child(2)").should(have.text('NCR Delhi'))
