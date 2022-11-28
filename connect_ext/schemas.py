# -*- coding: utf-8 -*-
#
# Copyright (c) 2022, Globex Corporation
# All rights reserved.
#
from typing import Optional

from pydantic import BaseModel, validator


class Marketplace(BaseModel):
    id: str
    name: str
    description: str
    icon: Optional[str]

    @validator('icon')
    def set_icon(cls, icon):
        return icon or '/static/images/mkp.svg'
