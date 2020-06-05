# Copyright 2020 Trayan Momkov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def init(driver_name):
    if driver_name == 'Firefox':
        driver = webdriver.Firefox(executable_path='./geckodriver')
    else:
        print('Unknown driver: "' + driver_name + '"')
        return

    driver.maximize_window()
    return driver


def find_by_text(element, text):
    elements = element.find_elements_by_xpath(".//*[contains(text(), '" + text + "')]")
    enabled_and_displayed = []
    for elem in elements:
        if elem.is_enabled() and elem.is_displayed():
            enabled_and_displayed.append(elem)
    return enabled_and_displayed


def find_first_by_text(element, text):
    elements = find_by_text(element, text)
    if elements:
        return elements[0]
    else:
        print('Cannot find element by text: "' + text + '"')


def find_first_parent_by_tag(element, tag):
    try:
        return element.find_element_by_xpath('./ancestor::' + tag)
    except NoSuchElementException as ex:
        print('Cannot find parent element by tag: "' + tag + '" ' + ex.msg)


def find_inputs(element):
    elements = element.find_elements_by_xpath(".//input")
    enabled_and_displayed = []
    for elem in elements:
        if elem.is_enabled() and elem.is_displayed():
            enabled_and_displayed.append(elem)
    return enabled_and_displayed


def find_first_input(element):
    elements = find_inputs(element)
    if elements:
        return elements[0]
    else:
        print('Cannot find input for the given element.')


def find_parent(element):
    try:
        return element.find_element_by_xpath("./..")
    except NoSuchElementException as ex:
        print('Cannot find parent of the given element. ' + ex.msg)


def find_input_for_label(element, label):
    try:
        return find_first_input(find_parent(find_first_by_text(element, label)))
    except NoSuchElementException as ex:
        print('Cannot find input for the given label: "' + label + '" ' + ex.msg)
