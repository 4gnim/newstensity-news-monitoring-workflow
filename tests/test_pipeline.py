import sys
from pathlib import Path
import unittest
import pandas as pd
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from data_processing import process_news
from sentiment_analysis import predict_sentiment

class TestProcessing(unittest.TestCase):
    def test_exact_duplicate_is_removed(self):
        row = {"article_id":"1", "source":"S", "published_at":"2026-01-01T00:00:00Z", "title":"Judul", "body":"Isi"}
        result, stats = process_news(pd.DataFrame([row, {**row, "article_id":"2"}]))
        self.assertEqual(len(result), 1)
        self.assertEqual(stats["duplicate_rows_removed"], 1)

    def test_missing_required_column_raises(self):
        with self.assertRaises(ValueError):
            process_news(pd.DataFrame([{ "article_id":"1" }]))

class TestSentimentBaseline(unittest.TestCase):
    def test_positive_cue(self):
        self.assertEqual(predict_sentiment("dukungan dan apresiasi")["sentiment_predicted"], "Positif")
    def test_negative_cue(self):
        self.assertEqual(predict_sentiment("kritik dan polemik")["sentiment_predicted"], "Negatif")
    def test_neutral_when_no_cue(self):
        self.assertEqual(predict_sentiment("jadwal rapat disampaikan hari ini")["sentiment_predicted"], "Netral")

if __name__ == "__main__":
    unittest.main()
