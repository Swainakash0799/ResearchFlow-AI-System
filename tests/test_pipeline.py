from unittest.mock import patch, Mock

from pipeline import run_research_pipeline


def test_run_research_pipeline():

    # Fake search agent
    fake_search_agent = Mock()
    fake_search_agent.invoke.return_value = {
        "messages": [
            Mock(content="Search results about AI")
        ]
    }

    # Fake reader agent
    fake_reader_agent = Mock()
    fake_reader_agent.invoke.return_value = {
        "messages": [
            Mock(content="Detailed scraped content about AI")
        ]
    }

    # Fake writer
    fake_writer = Mock()
    fake_writer.invoke.return_value = "Final AI research report"

    # Fake critic
    fake_critic = Mock()
    fake_critic.invoke.return_value = "Score: 8/10"

    with patch("pipeline.build_search_agent", return_value=fake_search_agent), \
         patch("pipeline.build_reader_agent", return_value=fake_reader_agent), \
         patch("pipeline.writer_chain", fake_writer), \
         patch("pipeline.critic_chain", fake_critic):

        result = run_research_pipeline("Artificial Intelligence")

    # Check final state
    assert isinstance(result, dict)

    assert "search_results" in result
    assert "scraped_content" in result
    assert "report" in result
    assert "feedback" in result

    assert result["search_results"] == "Search results about AI"
    assert result["scraped_content"] == "Detailed scraped content about AI"
    assert result["report"] == "Final AI research report"
    assert result["feedback"] == "Score: 8/10"