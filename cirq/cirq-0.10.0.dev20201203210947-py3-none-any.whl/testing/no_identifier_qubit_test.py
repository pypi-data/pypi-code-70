# Copyright 2020 The Cirq Developers
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import cirq


def test_named_qubit_repr():
    q = cirq.testing.NoIdentifierQubit()
    assert repr(q) == "cirq.testing.NoIdentifierQubit()"


def test_comparsion_key():
    q = cirq.testing.NoIdentifierQubit()
    p = cirq.testing.NoIdentifierQubit()
    assert p == q


def test_to_json():
    assert cirq.testing.NoIdentifierQubit()._json_dict_() == {
        'cirq_type': 'NoIdentifierQubit',
    }
