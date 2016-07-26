#!/usr/bin/env python
from marionette import Marionette
client = Marionette(host='localhost', port=2828)
client.start_session()
client.delete_session()
