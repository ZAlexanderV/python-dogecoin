# Copyright (c) 2010 Witchspace <witchspace81@gmail.com>
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
"""
dogecoin-python - Easy-to-use Dogecoin API client
"""

from dogecoinrpc.connection import DogecoinConnection
from dogecoinrpc.config import read_default_config


def connect_to_local(filename=None):
    """
    Connect to default dogecoin instance owned by this user, on this machine.

    Returns a :class:`~dogecoinrpc.connection.DogecoinConnection` object.

    Arguments:

        - `filename`: Path to a configuration file in a non-standard location (optional)
    """
    cfg = read_default_config(filename) or {}
    port = int(cfg.get("rpcport", "18332" if cfg.get("testnet") else "22555"))
    rpcuser = cfg.get("rpcuser", "")
    rpcpassword = cfg.get("rpcpassword", "")

    return DogecoinConnection(rpcuser, rpcpassword, "localhost", port)


def connect_to_remote(user, password, host="localhost", port=22555, use_https=False):
    """
    Connect to remote or alternative local dogecoin client instance.

    Returns a :class:`~dogecoinrpc.connection.DogecoinConnection` object.
    """
    return DogecoinConnection(user, password, host, port, use_https)
