"""Styling constants for the Digital Twin Gradio app."""

BLUE = "#3b82f6"
GREEN = "#22c55e"
NAVY = "#070b14"

# Keep the landing screen compact. These are intentionally short on mobile.
EXAMPLES = [
    "Who is Solomon?",
    "What are his strongest skills?",
    "What is he building now?",
    "How can I contact him?",
]

CSS = """
:root {
  --twin-blue: #3b82f6;
  --twin-blue-dark: #2563eb;
  --twin-green: #22c55e;
  --twin-bg: #070b14;
  --twin-glass: rgba(17, 24, 39, 0.62);
  --twin-surface: rgba(255, 255, 255, 0.045);
  --twin-border: rgba(255, 255, 255, 0.10);
  --twin-text: #f8fafc;
  --twin-muted: #94a3b8;
  --twin-placeholder: #64748b;
}

html,
body,
gradio-app {
  background:
    radial-gradient(circle at 50% -10%, rgba(59, 130, 246, .13), transparent 38%),
    radial-gradient(circle at 100% 45%, rgba(34, 197, 94, .055), transparent 30%),
    var(--twin-bg) !important;
  color: var(--twin-text) !important;
}

.gradio-container {
  background: transparent !important;
  color: var(--twin-text) !important;
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
  width: 100% !important;
  max-width: 960px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 38px 22px 42px !important;
}

.gradio-container .main,
.gradio-container .contain,
.gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}

.gradio-container * { min-width: 0; }

footer,
.built-with,
.show-api,
.api-docs { display: none !important; }

/* ---------- Header ---------- */
.gradio-container h1 {
  color: var(--twin-text) !important;
  font-size: 30px !important;
  font-weight: 760 !important;
  letter-spacing: -0.04em !important;
  margin: 0 0 7px !important;
  padding: 0 !important;
  text-align: left !important;
  border: 0 !important;
}

.gradio-container h1::after {
  content: "";
  display: block;
  width: 46px;
  height: 3px;
  margin-top: 11px;
  background: linear-gradient(90deg, var(--twin-blue) 0 58%, var(--twin-green) 58% 100%);
  border-radius: 999px;
}

.block,
.form { background: transparent !important; box-shadow: none !important; border: 0 !important; }

/* ---------- Chat surface ---------- */
.chatbot,
.chatbot.block {
  background:
    linear-gradient(145deg, rgba(255,255,255,.055), rgba(255,255,255,.018)),
    var(--twin-glass) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 22px !important;
  min-height: 500px !important;
  box-shadow:
    0 22px 60px rgba(0,0,0,.28),
    inset 0 1px 0 rgba(255,255,255,.055) !important;
  backdrop-filter: blur(18px) saturate(125%) !important;
  -webkit-backdrop-filter: blur(18px) saturate(125%) !important;
  overflow: hidden !important;
}

.chatbot::before {
  content: "";
  position: absolute;
  top: 0;
  left: 8%;
  right: 8%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,.18), transparent);
  pointer-events: none;
}

.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container { display: none !important; }

.chatbot .placeholder,
.chatbot .placeholder * { color: var(--twin-muted) !important; }

/* ---------- Message rows ---------- */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap,
.bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  max-width: 78% !important;
  font-size: 14px !important;
  line-height: 1.62 !important;
  padding: 11px 15px !important;
  border-radius: 17px !important;
  overflow-wrap: anywhere !important;
}

/* User: compact glossy blue bubble, never a tall narrow pill. */
.message-row.user-row,
.message-row[data-role="user"] { justify-content: flex-end !important; }

.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble,
.message-row[data-role="user"] .bubble {
  background: linear-gradient(145deg, rgba(59,130,246,.96), rgba(37,99,235,.88)) !important;
  color: #fff !important;
  border: 1px solid rgba(147,197,253,.20) !important;
  border-radius: 18px 18px 5px 18px !important;
  box-shadow:
    0 8px 24px rgba(37,99,235,.18),
    inset 0 1px 0 rgba(255,255,255,.13) !important;
}

/* Assistant: darker glass bubble with a very subtle highlight. */
.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble,
.message-row[data-role="assistant"] .bubble {
  background: linear-gradient(145deg, rgba(30,41,59,.74), rgba(15,23,42,.58)) !important;
  color: var(--twin-text) !important;
  border: 1px solid rgba(255,255,255,.075) !important;
  border-radius: 18px 18px 18px 5px !important;
  box-shadow:
    0 8px 24px rgba(0,0,0,.12),
    inset 0 1px 0 rgba(255,255,255,.045) !important;
}

/* Remove the old green left border completely. */
.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble,
.message-row[data-role="assistant"] .bubble {
  border-left: 1px solid rgba(255,255,255,.075) !important;
}

.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * { color: inherit !important; box-shadow: none !important; }

.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 14px !important;
  line-height: 1.62 !important;
  margin: 0 0 9px !important;
}

.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }

.message-row .message a,
.message-row .message-bubble a,
.message-row .bubble a {
  color: #60a5fa !important;
  text-decoration: underline !important;
}

/* ---------- Input ---------- */
.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] {
  align-items: stretch !important;
  gap: 9px !important;
  margin-top: 12px !important;
}

textarea,
input[type="text"] {
  background: linear-gradient(145deg, rgba(255,255,255,.055), rgba(255,255,255,.025)) !important;
  border: 1px solid var(--twin-border) !important;
  color: var(--twin-text) !important;
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
  font-size: 14px !important;
  line-height: 1.45 !important;
  padding: 13px 15px !important;
  min-height: 50px !important;
  border-radius: 15px !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.035) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
}

textarea:focus,
input[type="text"]:focus {
  border-color: rgba(59,130,246,.72) !important;
  outline: none !important;
  box-shadow: 0 0 0 3px rgba(59,130,246,.10), inset 0 1px 0 rgba(255,255,255,.055) !important;
}

textarea::placeholder,
input::placeholder { color: var(--twin-placeholder) !important; }

/* ---------- Buttons ---------- */
button {
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  border: 1px solid var(--twin-border) !important;
  background: rgba(255,255,255,.035) !important;
  color: var(--twin-text) !important;
  min-height: 50px !important;
  border-radius: 15px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  transition: .18s ease !important;
}

button:hover {
  border-color: rgba(96,165,250,.45) !important;
  color: #fff !important;
  background: rgba(255,255,255,.065) !important;
}

button:active { transform: translateY(1px) !important; }

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: linear-gradient(145deg, #3b82f6, #2563eb) !important;
  border: 1px solid rgba(147,197,253,.25) !important;
  color: #fff !important;
  min-height: 50px !important;
  min-width: 50px !important;
  border-radius: 15px !important;
  padding: 0 15px !important;
  box-shadow: 0 8px 24px rgba(37,99,235,.20), inset 0 1px 0 rgba(255,255,255,.14) !important;
}

button.primary:hover,
button[variant="primary"]:hover,
button.submit:hover,
button.submit-button:hover,
.submit-button:hover,
button.lg.primary:hover {
  background: linear-gradient(145deg, #60a5fa, #2563eb) !important;
}

button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 18px !important;
  height: 18px !important;
  margin: 0 auto !important;
  color: #fff !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ---------- Suggested questions ---------- */
.examples,
.examples-holder,
[data-testid="examples"] {
  background: transparent !important;
  padding: 0 !important;
  margin-top: 14px !important;
}

.examples table,
.examples-table { background: transparent !important; border: 0 !important; }

.examples button,
.example,
.examples td button,
[data-testid="examples"] button {
  background: rgba(255,255,255,.035) !important;
  border: 1px solid rgba(255,255,255,.085) !important;
  color: #cbd5e1 !important;
  font-size: 12px !important;
  font-weight: 450 !important;
  padding: 8px 11px !important;
  min-height: 0 !important;
  border-radius: 999px !important;
  box-shadow: inset 0 1px 0 rgba(255,255,255,.035) !important;
}

.examples button:hover,
.example:hover,
[data-testid="examples"] button:hover {
  border-color: rgba(96,165,250,.42) !important;
  color: #fff !important;
  background: rgba(59,130,246,.10) !important;
  transform: translateY(-1px) !important;
}

.icon-button,
.chatbot .icon-button {
  color: var(--twin-muted) !important;
  background: transparent !important;
  border: 0 !important;
  min-height: 0 !important;
  padding: 5px !important;
  border-radius: 8px !important;
}

.icon-button:hover,
.chatbot .icon-button:hover {
  color: #93c5fd !important;
  background: rgba(255,255,255,.05) !important;
}

::-webkit-scrollbar { width: 7px; height: 7px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(148,163,184,.28); border-radius: 999px; }
::-webkit-scrollbar-thumb:hover { background: rgba(96,165,250,.65); }

::selection { background: rgba(59,130,246,.70); color: #fff; }

/* ---------- Mobile ---------- */
@media (max-width: 640px) {
  .gradio-container { padding: 22px 11px 28px !important; }
  .gradio-container h1 { font-size: 23px !important; }
  .gradio-container h1::after { width: 40px; height: 3px; margin-top: 9px; }

  .chatbot,
  .chatbot.block {
    min-height: 455px !important;
    border-radius: 18px !important;
  }

  .message-row .message,
  .message-row .message-bubble,
  .message-row .bubble {
    max-width: 86% !important;
    font-size: 13.5px !important;
    line-height: 1.58 !important;
    padding: 10px 13px !important;
  }

  textarea,
  input[type="text"] {
    font-size: 14px !important;
    min-height: 48px !important;
    border-radius: 14px !important;
  }

  button.primary,
  button[variant="primary"],
  button.submit,
  button.submit-button,
  .submit-button,
  button.lg.primary {
    min-width: 48px !important;
    min-height: 48px !important;
    padding: 0 13px !important;
    border-radius: 14px !important;
  }

  /* Horizontal chips instead of a tall grid on phones. */
  .examples,
  .examples-holder,
  [data-testid="examples"] {
    margin-top: 10px !important;
    overflow-x: auto !important;
    overflow-y: hidden !important;
    white-space: nowrap !important;
    padding-bottom: 3px !important;
    scrollbar-width: none !important;
  }

  .examples::-webkit-scrollbar,
  .examples-holder::-webkit-scrollbar,
  [data-testid="examples"]::-webkit-scrollbar { display: none !important; }

  .examples button,
  .example,
  .examples td button,
  [data-testid="examples"] button {
    display: inline-flex !important;
    width: auto !important;
    margin-right: 5px !important;
    font-size: 11.5px !important;
    padding: 7px 10px !important;
  }
}

@media (max-width: 390px) {
  .gradio-container { padding-left: 8px !important; padding-right: 8px !important; }
  .chatbot, .chatbot.block { min-height: 430px !important; }
  .message-row .message,
  .message-row .message-bubble,
  .message-row .bubble { max-width: 90% !important; }
}
"""

JS = """
() => {
  document.title = 'Solomon | Digital Twin';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };

  setTimeout(focusInput, 400);

  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';

    let wasDisabled = area.disabled || area.readOnly;

    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, {
      attributes: true,
      attributeFilter: ['disabled', 'readonly']
    });
  };

  const scan = () => {
    document.querySelectorAll('textarea').forEach(watchTextarea);
  };

  setTimeout(scan, 600);

  new MutationObserver(scan).observe(document.body, {
    childList: true,
    subtree: true
  });
}
"""
