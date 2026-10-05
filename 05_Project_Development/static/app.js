async function api(url, options = {}) {
  const res = await fetch(url, options);
  const data = await res.json();
  if (!res.ok) throw new Error(data.error || "Something went wrong");
  return data;
}

function setLoading(id, loading) {
  const el = document.getElementById(id);
  el.textContent = loading ? "Thinking..." : "";
}

async function askQuestion() {
  const q = document.getElementById("question").value.trim();
  if (!q) return;
  setLoading("qnaResult", true);
  try {
    const data = await api("/qna?question=" + encodeURIComponent(q));
    document.getElementById("qnaResult").textContent = data.answer;
  } catch (e) { document.getElementById("qnaResult").textContent = e.message; }
}

async function explainTopic() {
  const topic = document.getElementById("topic").value.trim();
  if (!topic) return;
  setLoading("explanationResult", true);
  try {
    const data = await api("/explain", {
      method: "POST", headers: {"Content-Type": "application/json"},
      body: JSON.stringify({topic})
    });
    document.getElementById("explanationResult").textContent = data.explanation;
  } catch (e) { document.getElementById("explanationResult").textContent = e.message; }
}

async function summarizeText() {
  const text = document.getElementById("summaryText").value.trim();
  if (!text) return;
  setLoading("summaryResult", true);
  try {
    const data = await api("/summarize", {
      method: "POST", headers: {"Content-Type": "application/json"},
      body: JSON.stringify({text})
    });
    document.getElementById("summaryResult").textContent = data.summary;
  } catch (e) { document.getElementById("summaryResult").textContent = e.message; }
}

async function generateQuiz() {
  const text = document.getElementById("quizText").value.trim();
  if (!text) return;
  setLoading("quizResult", true);
  try {
    const data = await api("/quiz", {
      method: "POST", headers: {"Content-Type": "application/json"},
      body: JSON.stringify({text})
    });
    renderQuiz(data.quiz);
  } catch (e) { document.getElementById("quizResult").textContent = e.message; }
}

function renderQuiz(quiz) {
  const box = document.getElementById("quizResult");
  box.innerHTML = "";
  quiz.forEach((q, i) => {
    const div = document.createElement("div");
    div.className = "quiz-question";
    const title = document.createElement("div");
    title.innerHTML = `<strong>Q${i+1}. ${escapeHtml(q.question)}</strong>`;
    div.appendChild(title);

    q.options.forEach(option => {
      const label = document.createElement("label");
      label.className = "quiz-option";
      label.innerHTML = `<input type="radio" name="q${i}" value="${escapeHtml(option)}"> ${escapeHtml(option)}`;
      div.appendChild(label);
    });

    const btn = document.createElement("button");
    btn.textContent = "Check Answer";
    btn.onclick = () => {
      const selected = div.querySelector(`input[name="q${i}"]:checked`);
      if (!selected) return alert("Select an answer first.");
      const result = document.createElement("div");
      result.className = "correct";
      result.textContent = selected.value === q.answer
        ? "Correct!"
        : `Incorrect. Correct answer: ${q.answer}`;
      div.appendChild(result);
    };
    div.appendChild(btn);
    box.appendChild(div);
  });
}

async function getRecommendations() {
  const topic = document.getElementById("recommendTopic").value.trim();
  if (!topic) return;
  setLoading("recommendResult", true);
  try {
    const data = await api("/learn/recommendations?topic=" + encodeURIComponent(topic));
    document.getElementById("recommendResult").textContent = data.recommendation;
  } catch (e) { document.getElementById("recommendResult").textContent = e.message; }
}

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, ch => ({
    "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#039;"
  }[ch]));
}
