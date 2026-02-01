use pyo3::prelude::*;
use std::time::Instant;

/// Returns elapsed nanos between two dummy tokens.
/// Replace with real stream hook later.
#[pyfunction]
fn sample_drift() -> u128 {
    let start = Instant::now();
    // ⬇ placeholder for token gap
    std::thread::sleep(std::time::Duration::from_micros(15));
    start.elapsed().as_nanos()
}

#[pymodule]
fn μprobe(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sample_drift, m)?)?;
    Ok(())
}
