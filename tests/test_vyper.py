import pathlib
import textwrap

TEST_DIR = pathlib.Path(__file__).resolve().parent


def test_w3_fixture_is_available(request):
    from web3 import Web3
    from web3.providers.eth_tester import EthereumTesterProvider

    w3 = request.getfixturevalue("w3")
    assert isinstance(w3, Web3)
    assert isinstance(w3.provider, EthereumTesterProvider)
    assert w3.eth.gasPriceStrategy(None) == 0


def test_get_vyper_contract_fixture(testdir):
    """Make sure that pytest accepts our fixture."""

    # create a temporary pytest test module
    testdir.makepyfile(
        textwrap.dedent(
            f"""\
            import pathlib
            import pytest

            @pytest.fixture
            def contract_source():
                with open('{TEST_DIR.joinpath('example.vy')}') as f:
                    c_src = f.read()
                return c_src

            def test_initial_state(get_vyper_contract, contract_source):
                contract = get_vyper_contract(contract_source, 4)
                assert contract.storedData() == 4
            """
        )
    )

    # run pytest with the following cmd args
    result = testdir.runpytest("-v")

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(["*::test_initial_state PASSED*"])

    # make sure that that we get a '0' exit code for the testsuite
    assert result.ret == 0
