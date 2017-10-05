# Copyright (c) 2017 Joseph Wright <joseph@cloudboss.co>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
__metaclass__ = type


from ansible.errors import AnsibleFilterError
from ansible.module_utils.six.moves.urllib.parse import urlsplit
from ansible.utils import helpers
from friend import strings


def _thing_to_thing(formatter):
    def filtah(obj):
        try:
            if isinstance(obj, str):
                return formatter(obj)
            return strings.format_obj_keys(obj, formatter)
        except Exception as e:
            raise AnsibleFilterError(e)
    return filtah


class FilterModule(object):
    def filters(self):
        return {
            'snake_to_camel': _thing_to_thing(strings.snake_to_camel),
            'snake_to_pascal': _thing_to_thing(strings.snake_to_pascal),
            'camel_to_snake': _thing_to_thing(strings.camel_to_snake),
        }
