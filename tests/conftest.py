import pytest
from pytest_html import extras
import os


@pytest.fixture
def sample_numbers():
    return (10, 5)

def pytest_configure(config):
    config._metadata = getattr(config, "_metadata", {})
    config._metadata["Project"] = "QA Demo"
    config._metadata["Env"] = os.getenv("TEST_ENV", "local")
    config._metadata["Git SHA"] = os.getenv("GIT_SHA", "dev")

@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    report.title = "QA Test Report"

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["\n", "Executed by: QA Pipeline"])

@pytest.fixture(autouse=True)
def _init_extras(request):
    if not hasattr(request.node, "extra"):
        request.node.extra = []

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    # לצרף extras לטסטים
    if hasattr(report, "extra"):
        report.extra.extend(getattr(report, "extra", []))

def attach_text(request, text, name="note"):
    request.node.extra.append(extras.text(text, name=name))