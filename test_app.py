import pytest
import chromedriver_autoinstaller
from dash.testing.application_runners import import_app

# Auto install matching chromedriver
chromedriver_autoinstaller.install()

# Import the app
app = import_app("app")

def test_header_present(dash_duo):
    """Test 1: Check header is present"""
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)
    header = dash_duo.find_element("h1")
    assert header is not None
    assert "Pink Morsel" in header.text

def test_chart_present(dash_duo):
    """Test 2: Check line chart is present"""
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-chart", timeout=10)
    chart = dash_duo.find_element("#sales-chart")
    assert chart is not None

def test_region_picker_present(dash_duo):
    """Test 3: Check radio button region picker is present"""
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None