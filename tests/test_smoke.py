# -- encoding: UTF-8 --
"""
These tests do not verify any results and should not be run when
looking at improving test coverage.  They just verify that basic
operations don't fail due to odd corner cases on any locale that
we ship.
"""
from datetime import datetime

import pytest
from babel import Locale
from babel import dates
from babel import numbers
from babel._compat import Decimal


@pytest.mark.all_locales
def test_smoke_dates(locale):
    locale = Locale.parse(locale)
    instant = datetime.now()
    for width in ("full", "long", "medium", "short"):
        assert dates.format_date(instant, format=width, locale=locale)
        assert dates.format_datetime(instant, format=width, locale=locale)
        assert dates.format_time(instant, format=width, locale=locale)


@pytest.mark.all_locales
def test_smoke_numbers(locale):
    locale = Locale.parse(locale)
    for number in (
        Decimal("-33.76"),  # Negative Decimal
        Decimal("13.37"),  # Positive Decimal
        1.2 - 1.0,  # Inaccurate float
        10,  # Plain old integer
        0,  # Zero
    ):
        assert numbers.format_number(number, locale=locale)
