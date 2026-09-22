"""Styling constants for the Digital Twin Gradio app."""

BLUE = "#2563eb"
GREEN = "#16a34a"
NAVY = "#0f172a"

EXAMPLES = [
    "Who is Solomon and what is his background?",
    "What are Solomon's strongest technical skills?",
    "What data analytics and AI projects has Solomon worked on?",
    "What is Solomon currently learning and working toward?",
    "What experience does Solomon have in AI training and data annotation?",
    "What are Solomon's career goals?",
    "How can I get in touch with Solomon?",
]

CSS = """
:root {
  --twin-blue: #2563eb;
  --twin-blue-dark: #1d4ed8;
  --twin-green: #16a34a;
  --twin-green-dark: #15803d;
  --twin-navy: #0f172a;

  --twin-bg: #f8fafc;
  --twin-surface: #ffffff;
  --twin-surface-2: #f1f5f9;

  --twin-border: #e2e8f0;
  --twin-border-strong: #cbd5e1;

  --twin-text: #0f172a;
  --twin-muted: #64748b;
  --twin-placeholder: #94a3b8;
}

/* =========================================================
   LIGHT / DARK MODE
   ========================================================= */

/* Default light appearance */
body:not(.dark) {
  --twin-bg: #f8fafc;
  --twin-surface: #ffffff;
  --twin-surface-2: #f1f5f9;
  --twin-border: #e2e8f0;
  --twin-border-strong: #cbd5e1;
  --twin-text: #0f172a;
  --twin-muted: #64748b;
  --twin-placeholder: #94a3b8;
}

/* Dark appearance */
body.dark {
  --twin-bg: #0b1120;
  --twin-surface: #111827;
  --twin-surface-2: #172033;
  --twin-border: #243047;
  --twin-border-strong: #334155;
  --twin-text: #f1f5f9;
  --twin-muted: #94a3b8;
  --twin-placeholder: #64748b;
}

/* =========================================================
   HIDE DEFAULT GRADIO ELEMENTS
   ========================================================= */

footer,
.built-with,
.show-api,
.api-docs {
  display: none !important;
}

/* =========================================================
   GLOBAL PAGE
   ========================================================= */

html,
body,
gradio-app {
  background: var(--twin-bg) !important;
  color: var(--twin-text) !important;
}

.gradio-container {
  background: var(--twin-bg) !important;
  color: var(--twin-text) !important;

  font-family:
    Inter,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif !important;

  width: 100% !important;
  max-width: 920px !important;
  min-width: 0 !important;

  margin: 0 auto !important;
  padding: 42px 24px 56px !important;
}

.gradio-container .main,
.gradio-container .contain,
.gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}

.gradio-container * {
  min-width: 0;
}

/* =========================================================
   TITLE
   ========================================================= */

.gradio-container h1 {
  color: var(--twin-text) !important;

  font-size: 30px !important;
  font-weight: 750 !important;

  letter-spacing: -0.035em !important;

  margin: 0 0 8px !important;
  padding: 0 !important;

  text-align: left !important;

  border: 0 !important;
}

/* Small blue/green accent underneath title */
.gradio-container h1::after {
  content: "";
  display: block;

  width: 52px;
  height: 4px;

  margin-top: 12px;

  background: linear-gradient(
    90deg,
    var(--twin-blue) 0%,
    var(--twin-blue) 55%,
    var(--twin-green) 55%,
    var(--twin-green) 100%
  );

  border-radius: 999px;
}

/* =========================================================
   GENERAL BLOCK STYLING
   ========================================================= */

.block,
.form {
  background: transparent !important;
  box-shadow: none !important;
  border: 0 !important;
}

/* =========================================================
   CHATBOT
   ========================================================= */

.chatbot,
.chatbot.block {
  background: var(--twin-surface) !important;

  border: 1px solid var(--twin-border) !important;

  border-radius: 18px !important;

  min-height: 500px !important;

  box-shadow:
    0 8px 30px rgba(15, 23, 42, 0.06) !important;

  overflow: hidden !important;
}

/* =========================================================
   HIDE CHATBOT LABEL / HEADER
   ========================================================= */

.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

/* =========================================================
   CHATBOT PLACEHOLDER
   ========================================================= */

.chatbot .placeholder,
.chatbot .placeholder * {
  color: var(--twin-muted) !important;
}

/* =========================================================
   MESSAGE ROWS
   ========================================================= */

.message-row,
.message-row > div,
.message-row .role,
.message-wrap,
.bubble-wrap {
  background: transparent !important;

  border: 0 !important;

  box-shadow: none !important;
}

/* =========================================================
   MESSAGE BUBBLES
   ========================================================= */

.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  font-size: 14px !important;

  line-height: 1.6 !important;

  padding: 10px 14px !important;

  border-radius: 14px !important;

  border: 0 !important;

  box-shadow: none !important;
}

/* =========================================================
   USER MESSAGE
   ========================================================= */

.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: var(--twin-blue) !important;

  color: #ffffff !important;

  border-radius: 16px 16px 4px 16px !important;
}

/* =========================================================
   ASSISTANT MESSAGE
   ========================================================= */

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-surface-2) !important;

  color: var(--twin-text) !important;

  border-radius: 16px 16px 16px 4px !important;

  border-left: 3px solid var(--twin-green) !important;
}

/* =========================================================
   REMOVE DUPLICATE ASSISTANT BORDERS
   ========================================================= */

.message-row.bot-row .message .message,
.message-row.bot-row .message .bubble,
.message-row.bot-row .message .message-bubble,

.message-row.bot-row .bubble .message,
.message-row.bot-row .bubble .bubble,
.message-row.bot-row .bubble .message-bubble,

.message-row.bot-row .message-bubble .message,
.message-row.bot-row .message-bubble .bubble,
.message-row.bot-row .message-bubble .message-bubble,

.message-row[data-role="assistant"] .message .message,
.message-row[data-role="assistant"] .message .bubble,
.message-row[data-role="assistant"] .message .message-bubble,

.message-row[data-role="assistant"] .bubble .message,
.message-row[data-role="assistant"] .bubble .bubble,
.message-row[data-role="assistant"] .bubble .message-bubble,

.message-row[data-role="assistant"] .message-bubble .message,
.message-row[data-role="assistant"] .message-bubble .bubble,
.message-row[data-role="assistant"] .message-bubble .message-bubble {
  border-left: 0 !important;
}

/* =========================================================
   MESSAGE TEXT
   ========================================================= */

.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  font-size: 14px !important;
  line-height: 1.6 !important;
}

.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 14px !important;

  line-height: 1.6 !important;

  margin: 0 0 9px !important;

  color: inherit !important;
}

.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child {
  margin-bottom: 0 !important;
}

/* =========================================================
   CONTENT INSIDE BUBBLES
   ========================================================= */

.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  color: inherit !important;

  box-shadow: none !important;
}

/* Keep links visible */
.message-row .message a,
.message-row .message-bubble a,
.message-row .bubble a {
  color: var(--twin-blue) !important;

  text-decoration: underline !important;

  text-decoration-thickness: 1px !important;
}

/* =========================================================
   INPUT AREA
   ========================================================= */

.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] {
  align-items: stretch !important;

  gap: 10px !important;
}

/* =========================================================
   TEXT INPUT
   ========================================================= */

textarea,
input[type="text"] {
  background: var(--twin-surface) !important;

  border: 1px solid var(--twin-border) !important;

  color: var(--twin-text) !important;

  font-family:
    Inter,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif !important;

  font-size: 14px !important;

  line-height: 1.45 !important;

  padding: 13px 15px !important;

  min-height: 50px !important;

  border-radius: 12px !important;

  transition:
    border-color 0.15s ease,
    box-shadow 0.15s ease !important;
}

textarea:focus,
input[type="text"]:focus {
  border-color: var(--twin-blue) !important;

  outline: none !important;

  box-shadow:
    0 0 0 3px rgba(37, 99, 235, 0.10) !important;
}

textarea::placeholder,
input::placeholder {
  color: var(--twin-placeholder) !important;
}

/* =========================================================
   BUTTONS
   ========================================================= */

button {
  font-family:
    Inter,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif !important;

  letter-spacing: 0 !important;

  text-transform: none !important;

  font-size: 13px !important;

  font-weight: 600 !important;

  border: 1px solid var(--twin-border) !important;

  background: var(--twin-surface) !important;

  color: var(--twin-text) !important;

  padding: 0 17px !important;

  min-height: 50px !important;

  border-radius: 12px !important;

  align-self: stretch !important;

  display: inline-flex !important;

  align-items: center !important;

  justify-content: center !important;

  cursor: pointer !important;

  transition:
    background 0.15s ease,
    color 0.15s ease,
    border-color 0.15s ease,
    transform 0.15s ease !important;
}

button:hover {
  border-color: var(--twin-blue) !important;

  color: var(--twin-blue) !important;

  background: var(--twin-surface) !important;
}

button:active {
  transform: translateY(1px) !important;
}

/* =========================================================
   PRIMARY / SEND BUTTON
   ========================================================= */

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: var(--twin-blue) !important;

  border: 1px solid var(--twin-blue) !important;

  color: #ffffff !important;

  min-height: 50px !important;

  border-radius: 12px !important;

  padding: 0 17px !important;

  display: inline-flex !important;

  align-items: center !important;

  justify-content: center !important;
}

button.primary:hover,
button[variant="primary"]:hover,
button.submit:hover,
button.submit-button:hover,
.submit-button:hover,
button.lg.primary:hover {
  background: var(--twin-blue-dark) !important;

  border-color: var(--twin-blue-dark) !important;

  color: #ffffff !important;
}

/* =========================================================
   SUBMIT BUTTON ICON
   ========================================================= */

button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 18px !important;

  height: 18px !important;

  margin: 0 auto !important;

  display: block !important;

  align-self: center !important;

  color: #ffffff !important;

  fill: currentColor !important;

  stroke: currentColor !important;
}

/* =========================================================
   EXAMPLES
   ========================================================= */

.examples,
.examples-holder,
[data-testid="examples"] {
  background: transparent !important;

  padding: 0 !important;

  margin-top: 18px !important;
}

.examples table,
.examples-table {
  background: transparent !important;

  border: 0 !important;
}

/* =========================================================
   EXAMPLE BUTTONS
   ========================================================= */

.examples button,
.example,
.examples td button,
[data-testid="examples"] button {
  background: var(--twin-surface) !important;

  border: 1px solid var(--twin-border) !important;

  color: var(--twin-text) !important;

  text-transform: none !important;

  letter-spacing: 0 !important;

  font-family:
    Inter,
    -apple-system,
    BlinkMacSystemFont,
    "Segoe UI",
    sans-serif !important;

  font-size: 13px !important;

  font-weight: 450 !important;

  padding: 10px 13px !important;

  text-align: left !important;

  min-height: 0 !important;

  border-radius: 10px !important;

  align-self: auto !important;

  display: inline-block !important;

  transition:
    border-color 0.15s ease,
    background 0.15s ease,
    color 0.15s ease,
    transform 0.15s ease !important;
}

.examples button:hover,
.example:hover,
[data-testid="examples"] button:hover {
  border-color: var(--twin-blue) !important;

  color: var(--twin-blue) !important;

  background: var(--twin-surface) !important;

  transform: translateY(-1px) !important;
}

/* =========================================================
   ICON BUTTONS
   ========================================================= */

.icon-button,
.chatbot .icon-button {
  color: var(--twin-muted) !important;

  background: transparent !important;

  border: 0 !important;

  min-height: 0 !important;

  align-self: auto !important;

  padding: 5px !important;

  border-radius: 8px !important;

  display: inline-flex !important;

  align-items: center !important;

  justify-content: center !important;
}

.icon-button:hover,
.chatbot .icon-button:hover {
  color: var(--twin-blue) !important;

  background: var(--twin-surface-2) !important;
}

/* =========================================================
   SCROLLBAR
   ========================================================= */

::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: var(--twin-bg);
}

::-webkit-scrollbar-thumb {
  background: var(--twin-border-strong);

  border-radius: 999px;
}

::-webkit-scrollbar-thumb:hover {
  background: var(--twin-blue);
}

/* =========================================================
   TEXT SELECTION
   ========================================================= */

::selection {
  background: var(--twin-blue);

  color: #ffffff;
}

/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 640px) {

  .gradio-container {
    padding: 24px 14px 40px !important;
  }

  .gradio-container h1 {
    font-size: 24px !important;
  }

  .chatbot,
  .chatbot.block {
    min-height: 460px !important;

    border-radius: 14px !important;
  }

  textarea,
  input[type="text"] {
    font-size: 14px !important;

    min-height: 48px !important;
  }

  button {
    min-height: 48px !important;
  }

  .examples button,
  .example,
  .examples td button,
  [data-testid="examples"] button {
    font-size: 12px !important;

    padding: 9px 11px !important;
  }
}
"""

JS = """
() => {
  document.title = 'Solomon | Digital Twin';

  /* -------------------------------------------------------
     Focus the message input when the app loads
     ------------------------------------------------------- */

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');

    if (areas.length) {
      areas[areas.length - 1].focus();
    }
  };

  setTimeout(focusInput, 400);


  /* -------------------------------------------------------
     Re-focus the message field after the assistant responds
     ------------------------------------------------------- */

  const watchTextarea = (area) => {

    if (area.dataset.twinWatched) {
      return;
    }

    area.dataset.twinWatched = '1';

    let wasDisabled =
      area.disabled ||
      area.readOnly;

    new MutationObserver(() => {

      const isDisabled =
        area.disabled ||
        area.readOnly;

      if (wasDisabled && !isDisabled) {
        area.focus();
      }

      wasDisabled = isDisabled;

    }).observe(area, {
      attributes: true,
      attributeFilter: [
        'disabled',
        'readonly'
      ]
    });
  };


  /* -------------------------------------------------------
     Detect newly-created Gradio textareas
     ------------------------------------------------------- */

  const scan = () => {

    document
      .querySelectorAll('textarea')
      .forEach(watchTextarea);

  };

  setTimeout(scan, 600);


  new MutationObserver(scan).observe(
    document.body,
    {
      childList: true,
      subtree: true
    }
  );
}
"""