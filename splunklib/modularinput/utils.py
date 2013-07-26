# Copyright 2011-2013 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# File for utility functions

def xml_compare(expected, found):
    """Checks equality of two ElementTree objects

    :param expected: an ElementTree object
    :param found: an ElementTree object
    :return: boolean, equality of expected and found
    """

    # if comparing the same ET object
    if expected == found:
        return True

    # compare element attributes, ignoring order
    if set(expected.items()) != set(found.items()):
        return False

    # check for equal number of children
    expected_children = list(expected)
    found_children = list(found)
    if len(expected_children) != len(found_children):
        return False

    # compare children
    if not all([xml_compare(a, b) for a, b in zip(expected_children, found_children)]):
        return False

    # compare elements, if there is no text node, return True
    if (expected.text is None or expected.text.strip() == "") and (found.text is None or found.text.strip() == ""):
        return True
    else:
        return expected.tag == found.tag and expected.text == found.text and expected.attrib == found.attrib