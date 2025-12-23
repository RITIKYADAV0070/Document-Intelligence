import React, { useState } from "react";
import { runExtraction } from "./api";
import "./styles.css";

export default function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [showJson, setShowJson] = useState(true);

  const handleRun = async () => {
    setLoading(true);
    setError("");
    try {
      const result = await runExtraction();
      setData(result);
      setShowJson(true);
    } catch (e) {
      setError("Failed to fetch data from API");
    } finally {
      setLoading(false);
    }
  };

  const downloadJson = () => {
    const blob = new Blob([JSON.stringify(data, null, 2)], {
      type: "application/json",
    });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "document_intelligence_output.json";
    a.click();
    URL.revokeObjectURL(url);
  };

  const copyJson = async () => {
    await navigator.clipboard.writeText(
      JSON.stringify(data, null, 2)
    );
    alert("JSON copied to clipboard");
  };

  const getConfidenceColor = (confidence) => {
    const percent = Math.round((confidence || 0) * 100);
    if (percent < 40) return "#ef4444";
    if (percent < 70) return "#facc15";
    return "#22c55e";
  };

  return (
    <div className="app">
      {/* Header */}
      <header className="header">
        <h1>📄 Document Intelligence</h1>
        <p>AI-based extraction of CRIF & GSTR-3B financial documents</p>
      </header>

      {/* Action Bar */}
      <div className="action-bar">
        <button onClick={handleRun} disabled={loading}>
          {loading ? "Extracting..." : "Run Extraction"}
        </button>

        {data && (
          <>
            <button className="secondary" onClick={downloadJson}>
              ⬇ Download JSON
            </button>

            <button className="secondary" onClick={copyJson}>
              📋 Copy JSON
            </button>

            <button
              className="secondary"
              onClick={() => setShowJson(!showJson)}
            >
              {showJson ? "Hide Raw JSON" : "View Raw JSON"}
            </button>

            <div className="confidence-badge">
              Overall Confidence:{" "}
              <strong>
                {Math.round(data.overall_confidence_score * 100)}%
              </strong>
            </div>
          </>
        )}
      </div>

      {error && <p className="error">{error}</p>}

      {/* RAW JSON — TOP */}
      {showJson && data && (
        <section className="section">
          <h2>🧾 Raw JSON Output</h2>
          <pre className="json-viewer">
            {JSON.stringify(data, null, 2)}
          </pre>
        </section>
      )}

      {/* CRIF SECTION */}
      {data?.bureau_parameters && (
        <section className="section">
          <h2>🏦 CRIF Bureau Parameters</h2>

          <div className="grid">
            {Object.entries(data.bureau_parameters).map(
              ([key, param]) => {
                const percent = Math.round(
                  (param.confidence || 0) * 100
                );

                return (
                  <div key={key} className="card">
                    <h3>{key.replaceAll("_", " ")}</h3>

                    <p className="value">
                      {param.value === null
                        ? "Not Found"
                        : param.value}
                    </p>

                    <p className="source">
                      {param.source || "not_found"}
                    </p>

                    <div className="confidence">
                      <div
                        className="confidence-bar"
                        style={{
                          width: `${percent}%`,
                          background: getConfidenceColor(
                            param.confidence
                          ),
                        }}
                      />
                    </div>

                    <span className="confidence-label">
                      Confidence: {percent}%
                    </span>
                  </div>
                );
              }
            )}
          </div>
        </section>
      )}

      {/* GST SECTION */}
      {data?.gst_sales && (
        <section className="section">
          <h2>📈 GSTR-3B Monthly Sales</h2>

          <table>
            <thead>
              <tr>
                <th>Month</th>
                <th>Sales (₹)</th>
                <th>Source</th>
                <th>Confidence</th>
              </tr>
            </thead>
            <tbody>
              {data.gst_sales.map((row, idx) => (
                <tr key={idx}>
                  <td>{row.month}</td>
                  <td>
                    {row.sales.toLocaleString("en-IN")}
                  </td>
                  <td>{row.source}</td>
                  <td
                    style={{
                      color: getConfidenceColor(
                        row.confidence
                      ),
                      fontWeight: 600,
                    }}
                  >
                    {Math.round(row.confidence * 100)}%
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>
      )}
    </div>
  );
}
