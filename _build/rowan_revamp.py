"""Revamp the three problem sections of rowan/index.html"""
import pathlib, re

BASE = pathlib.Path('C:/Users/cczin/code/hedgerow.dev')
f = BASE / 'rowan/index.html'
c = f.read_text(encoding='utf-8')

# ── 1. Replace code-block section with single clean taint trace ──────────────
# Find the section from <!-- The problem --> to its closing </section>
OLD_START = '<!-- The problem -->'
NEW_SECTION = '''<!-- The problem -->
<section style="background:var(--bg);padding:5rem 0;border-bottom:1px solid var(--border)">
  <div class="wrap">
    <p class="section-label">The limitation</p>
    <h2>Real vulnerabilities don&rsquo;t stay in one file.</h2>
    <p style="color:var(--muted);max-width:640px;line-height:1.8;margin-bottom:2.5rem">An SSRF that spans two files and an async method won&rsquo;t appear in a single-file regex scan. Rowan follows the full chain and shows exactly where it breaks.</p>
    <div class="code-block" style="display:block;max-width:680px">
      <div style="color:#E87070;font-weight:600;margin-bottom:1.25rem">[CRITICAL] Server-Side Request Forgery &mdash; confidence: 89%</div>
      <div style="display:grid;grid-template-columns:4.5rem 1fr;row-gap:.55rem;align-items:baseline">
        <span style="color:var(--faint);font-size:.7rem;text-transform:uppercase;letter-spacing:.07em">Source</span>
        <span style="font-size:.8rem"><span style="color:#8FA3AC">api/endpoints.py:3</span><span style="color:var(--faint)"> &nbsp; url = request.args.get(&lsquo;url&rsquo;)</span></span>
        <span style="color:var(--faint);font-size:.7rem;text-transform:uppercase;letter-spacing:.07em">Via</span>
        <span style="font-size:.8rem"><span style="color:#8FA3AC">api/endpoints.py:5</span><span style="color:var(--faint)"> &nbsp; return await client.get(url)</span></span>
        <span style="color:var(--faint);font-size:.7rem;text-transform:uppercase;letter-spacing:.07em">Sink</span>
        <span style="font-size:.8rem"><span style="color:#8FA3AC">clients/resource.py:9</span><span style="color:#E87070"> &nbsp; httpx.get(url) &mdash; no validation</span></span>
      </div>
      <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid rgba(255,255,255,.07);color:var(--faint);font-size:.78rem">No URL validation, scheme restriction, or allowlist detected.</div>
    </div>
  </div>
</section>'''

# Replace from <!-- The problem --> to its closing </section>
pattern = re.compile(
    r'<!-- The problem -->.*?</section>',
    re.DOTALL
)
c = pattern.sub(NEW_SECTION, c, count=1)
print('limitation section: replaced')

# ── 2. Replace 6 coverage cards → scannable 2-col grid ───────────────────────
COV_START = '<!-- What Rowan covers -->'
NEW_COV = '''<!-- What Rowan covers -->
<section id="coverage" style="background:var(--surface);padding:5rem 0;border-bottom:1px solid var(--border)">
  <div class="wrap">
    <p class="section-label">Coverage</p>
    <h2>What Rowan tracks.</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;margin-top:2.5rem;max-width:860px;border-top:1px solid var(--border)">
      <div style="padding:1.25rem 2rem 1.25rem 0;border-bottom:1px solid var(--border);border-right:1px solid var(--border)">
        <p style="font-weight:600;color:var(--navy);font-size:.9rem;margin-bottom:.3rem">Cross-file taint</p>
        <p style="font-size:.875rem;margin:0">HTTP params, CLI args, env vars &mdash; followed to dangerous sinks across files and function boundaries.</p>
      </div>
      <div style="padding:1.25rem 0 1.25rem 2rem;border-bottom:1px solid var(--border)">
        <p style="font-weight:600;color:var(--navy);font-size:.9rem;margin-bottom:.3rem">AI/ML sink models</p>
        <p style="font-size:.875rem;margin:0"><code>torch.load()</code>, <code>trust_remote_code=True</code>, <code>apply_chat_template()</code> &mdash; modelled as distinct attack surfaces.</p>
      </div>
      <div style="padding:1.25rem 2rem 1.25rem 0;border-bottom:1px solid var(--border);border-right:1px solid var(--border)">
        <p style="font-weight:600;color:var(--navy);font-size:.9rem;margin-bottom:.3rem">Model file scanning</p>
        <p style="font-size:.875rem;margin:0">Static analysis of checkpoint files, GGUF, SafeTensors, and Keras <code>.h5</code> before they are loaded.</p>
      </div>
      <div style="padding:1.25rem 0 1.25rem 2rem;border-bottom:1px solid var(--border)">
        <p style="font-weight:600;color:var(--navy);font-size:.9rem;margin-bottom:.3rem">Reachability-aware SCA</p>
        <p style="font-size:.875rem;margin:0">Only surfaces CVEs your code can actually trigger. Unreachable vulnerabilities are suppressed.</p>
      </div>
      <div style="padding:1.25rem 2rem 1.25rem 0;border-right:1px solid var(--border)">
        <p style="font-weight:600;color:var(--navy);font-size:.9rem;margin-bottom:.3rem">Prompt injection</p>
        <p style="font-size:.875rem;margin:0">Taint flows into LLM system prompts, RAG contexts, and Jinja2 template rendering.</p>
      </div>
      <div style="padding:1.25rem 0 1.25rem 2rem">
        <p style="font-weight:600;color:var(--navy);font-size:.9rem;margin-bottom:.3rem">Framework patterns</p>
        <p style="font-size:.875rem;margin:0">Named rules for LangChain, Keras importlib, OmegaConf, ONNX Hub, Gradio, and others.</p>
      </div>
    </div>
  </div>
</section>'''

pattern2 = re.compile(r'<!-- What Rowan covers -->.*?</section>', re.DOTALL)
c = pattern2.sub(NEW_COV, c, count=1)
print('coverage section: replaced')

# ── 3. Replace four engines → tight numbered list ────────────────────────────
ARCH_START = '<!-- Four engines -->'
NEW_ARCH = '''<!-- Four engines -->
<section id="architecture" style="background:var(--bg);padding:5rem 0;border-bottom:1px solid var(--border)">
  <div class="wrap">
    <p class="section-label">Architecture</p>
    <h2>Four engines, running in parallel.</h2>
    <div style="display:flex;flex-direction:column;margin-top:2.5rem;max-width:780px;border-top:1px solid var(--border)">
      <div style="display:grid;grid-template-columns:2rem 8rem 1fr;gap:0 1.5rem;padding:1.25rem 0;border-bottom:1px solid var(--border);align-items:baseline">
        <span style="font-size:.82rem;font-weight:700;color:var(--sage)">1</span>
        <span style="font-weight:600;color:var(--navy);font-size:.9rem">CodeGuard</span>
        <span style="font-size:.9rem;color:var(--muted)">Inter-procedural taint &mdash; follows user input across files, imports, and function calls.</span>
      </div>
      <div style="display:grid;grid-template-columns:2rem 8rem 1fr;gap:0 1.5rem;padding:1.25rem 0;border-bottom:1px solid var(--border);align-items:baseline">
        <span style="font-size:.82rem;font-weight:700;color:var(--sage)">2</span>
        <span style="font-weight:600;color:var(--navy);font-size:.9rem">NeuroScan</span>
        <span style="font-size:.9rem;color:var(--muted)">125+ AST pattern rules &mdash; secrets, missing auth, AI framework misconfigurations, known CVE patterns.</span>
      </div>
      <div style="display:grid;grid-template-columns:2rem 8rem 1fr;gap:0 1.5rem;padding:1.25rem 0;border-bottom:1px solid var(--border);align-items:baseline">
        <span style="font-size:.82rem;font-weight:700;color:var(--sage)">3</span>
        <span style="font-weight:600;color:var(--navy);font-size:.9rem">DepGuard</span>
        <span style="font-size:.9rem;color:var(--muted)">Supply chain with reachability &mdash; only reports CVEs your code can actually trigger.</span>
      </div>
      <div style="display:grid;grid-template-columns:2rem 8rem 1fr;gap:0 1.5rem;padding:1.25rem 0;align-items:baseline">
        <span style="font-size:.82rem;font-weight:700;color:var(--sage)">4</span>
        <span style="font-weight:600;color:var(--navy);font-size:.9rem">Huntr Agent</span>
        <span style="font-size:.9rem;color:var(--muted)">Autonomous hypothesis generation, exploit confirmation, and full write-up &mdash; no manual triage.</span>
      </div>
    </div>
  </div>
</section>'''

pattern3 = re.compile(r'<!-- Four engines -->.*?</section>', re.DOTALL)
c = pattern3.sub(NEW_ARCH, c, count=1)
print('architecture section: replaced')

f.write_text(c, encoding='utf-8')
print('rowan/index.html saved')
