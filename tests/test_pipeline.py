def test_pipeline_returns_routing_and_metrics(trained_pipeline, sample_ticket):
    result = trained_pipeline.process(sample_ticket)

    assert "assigned_to" in result
    assert result["category"] in ["Billing", "Tech", "Account", "Bug", "Feature"]
    assert 0.0 <= result["confidence"] <= 1.0
    assert "metrics_summary" in result
    assert result["metrics_summary"]["total_processed"] >= 1
