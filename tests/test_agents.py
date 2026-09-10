from agents import (
    build_search_agent,
    build_reader_agent,
    writer_chain,
    critic_chain
)


def test_build_search_agent():
    agent = build_search_agent()
    assert agent is not None


def test_build_reader_agent():
    agent = build_reader_agent()
    assert agent is not None


def test_writer_chain_exists():
    assert writer_chain is not None


def test_critic_chain_exists():
    assert critic_chain is not None