#!/usr/bin/env python
'''class inherent of BaseModel'''


class State(BaseModel):
    '''class State'''
    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__

        self.name = ""
