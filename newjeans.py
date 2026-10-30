"""실행: python -m streamlit run app.py"""

from html import escape
from pathlib import Path

import streamlit as st

from careers import CAREERS


st.set_page_config(
    page_title="NEXT TRACK | 데이터·AI 커리어 클럽",
    page_icon="💿",
    layout="wide",
    initial_sidebar_state="expanded",
)


def html(markup):
    """앱이 작성한 마크업만 전달합니다. 동적 텍스트는 escape 처리합니다."""
    st.markdown(markup, unsafe_allow_html=True)


def label(kicker, title, description=""):
    html(f'<div class="section-label">{escape(kicker)}</div>')
    st.subheader(title)
    if description:
        st.write(description)


def card(title, body, number="", class_name="note-card"):
    html(
        f'<article class="{class_name}">'
        f'<span class="card-number">{escape(number)}</span>'
        f'<h3>{escape(title)}</h3><p>{escape(body)}</p></article>'
    )


def career_note(name, job):
    lines = [f"{name} / {job['en']}", "", job["intro"], "", "[구체적인 업무]"]
    for title, body in job["tasks"]:
        lines.append(f"- {title}: {body}")
    lines += ["", "[주요 기술 스택]"]
    for group, items in job["stack"].items():
        lines.append(group)
        lines.extend(f"- {tool}: {purpose}" for tool, purpose in items)
    lines += ["", "[중요한 역량]"]
    lines.extend(f"- {title}: {body}" for title, body in job["skills"])
    case = job["case"]
    lines += ["", f"[실무 예시] {case['title']}", case["problem"]]
    lines.extend(f"{i}. {step}" for i, step in enumerate(case["steps"], 1))
    lines += [f"산출물: {case['deliverable']}", f"확인 지표: {case['metric']}", "", "[시작하는 순서]"]
    lines.extend(f"{i}. {step}" for i, step in enumerate(job["roadmap"], 1))
    lines += ["", "[포트폴리오 아이디어]", job["portfolio"], "", "[직무 범위 참고]", job["boundary"]]
    return "\n".join(lines)


html(f"<style>{Path(__file__).with_name('style.css').read_text(encoding='utf-8')}</style>")

def go_home():
    st.session_state["career"] = None


with st.sidebar:
    st.button("next track", key="home", on_click=go_home)
    html('<div class="side-brand"><span>DATA & AI CAREER CLUB</span></div>')
    html('<div class="side-sticker">✦ YOUR NEXT CHAPTER ✦</div>')
    st.caption("어떤 일을 하는지부터, 나의 다음 트랙을 찾아봐요.")
    selected = st.radio(
        "탐색할 직업",
        options=list(CAREERS),
        index=None,
        format_func=lambda name: f"{CAREERS[name]['icon']}  {name}",
        captions=[job["short"] for job in CAREERS.values()],
        key="career",
    )
    st.divider()
    st.caption("💡 모바일에서는 왼쪽 위 메뉴 버튼으로 직업 목록을 열 수 있어요.")
    html('<div class="side-footer">7 TRACKS · ENDLESS POSSIBILITIES<br>조금씩 알아가도 괜찮아. ♡</div>')

html('''<div class="masthead"><span>✳ NEXT TRACK / CAREER EDITION</span>
<span>DATA · AI · YOU</span></div>''')

if selected is None:
    html('''
<section class="hero">
  <div class="hero-copy"><span class="eyebrow">A LITTLE CURIOUS, A LITTLE BRAVE</span>
    <h1>너의 다음 트랙은,<br><em>어떤 모습일까?</em></h1>
    <p>데이터와 AI로 일하는 일곱 가지 방법.<br>좋아하는 일을 발견하는 작은 커리어 플레이리스트.</p>
    <div class="hero-tags"><span>7 careers</span><span>real work</span><span>find your track ♡</span></div>
  </div>
  <div class="disc-art" aria-hidden="true"><div class="orbit">✧</div><div class="disc"><div class="disc-center">NEXT<br>TRACK</div></div>
    <span class="art-label">PLAY YOUR<br>POSSIBILITIES ↗</span><span class="little-star">✳</span></div>
</section>''')
    st.write("")
    st.info("왼쪽 사이드바에서 탐색할 직업을 선택해 보세요. 소개부터 실무와 핵심 역량까지 알아볼 수 있어요.", icon="💿")
    st.stop()

job = CAREERS[selected]
track = list(CAREERS).index(selected) + 1

html(
    f'<section class="track-header" style="--track-color:{job["color"]}">'
    f'<div class="track-icon" aria-hidden="true">{job["icon"]}</div>'
    f'<div><span class="eyebrow">TRACK {track:02d} / 07 · {escape(job["group"])}</span>'
    f'<h2>{escape(selected)}</h2><span class="english-name">{escape(job["en"])}</span></div>'
    f'<span class="track-stamp">NOW<br>EXPLORING ♡</span></section>'
)

intro, tasks, stack, skills, project = st.tabs(
    ["01  직업 소개", "02  구체적인 업무", "03  기술 스택", "04  핵심 역량", "05  실무 & 시작하기"]
)

with intro:
    label("MEET YOUR TRACK", job["tagline"], job["intro"])
    html(f'<div class="question-box"><span>이 직업이 답하는 질문</span><p>“{escape(job["question"])}”</p></div>')
    left, right = st.columns(2, gap="medium")
    with left:
        card("이런 일에 마음이 간다면", job["fit"], "♡")
    with right:
        card("함께 만드는 결과물", job["case"]["deliverable"], "↗")
    st.info(job["boundary"], icon="💡")

with tasks:
    label("BEHIND THE JOB", "실제로는 이런 일을 해요", "하나의 문제를 받아 결과를 내기까지, 대표적인 업무 흐름을 따라가 보세요.")
    for i, (title, body) in enumerate(job["tasks"], 1):
        html(f'<article class="work-row"><span class="work-index">{i:02d}</span><div><h3>{escape(title)}</h3><p>{escape(body)}</p></div></article>')
    st.caption("업무 흐름을 이해하기 위한 예시입니다. 모든 조직에서 같은 순서나 비중으로 일하지는 않습니다.")

with stack:
    label("TOOLS IN YOUR BAG", "도구보다 먼저, 쓰는 이유를 알아요", "대표적인 도구의 예시입니다. 모두 배워야 하는 목록은 아니며, 같은 목적의 도구는 팀마다 달라요.")
    for column, (group, tools) in zip(st.columns(2, gap="large"), job["stack"].items()):
        with column:
            st.markdown(f"#### {group}")
            for tool, purpose in tools:
                card(tool, purpose, "✦", "tool-card")

with skills:
    label("MORE THAN TOOLS", "오래 가져갈, 나만의 실력", "도구를 다루는 능력과 함께, 문제를 바라보고 협업하는 방식도 중요해요.")
    columns = st.columns(2, gap="medium")
    for i, (title, body) in enumerate(job["skills"]):
        with columns[i % 2]:
            card(title, body, f"0{i + 1}")
    html('<div class="small-callout">✧ 포트폴리오에는 결과뿐 아니라 <strong>왜 그렇게 판단했는지</strong>도 남겨 보세요.</div>')

with project:
    case = job["case"]
    label("A DAY IN THE REAL WORLD", case["title"])
    st.write(f"**상황** · {case['problem']}")
    for i, step in enumerate(case["steps"], 1):
        st.markdown(f"**{i:02d}.** {step}")
    left, right = st.columns(2)
    with left:
        card("남기는 결과물", case["deliverable"], "OUTPUT")
    with right:
        card("확인하는 지표", case["metric"], "CHECK")
    st.divider()
    label("YOUR FIRST STEPS", "처음 시작한다면, 이 순서로")
    for i, step in enumerate(job["roadmap"], 1):
        st.markdown(f"**STEP {i}** · {step}")
    st.success(job["portfolio"], icon="🌱")

st.write("")
st.download_button(
    "↓ 이 직업의 커리어 노트 저장",
    data=career_note(selected, job),
    file_name=f"{selected}_커리어노트.txt",
    mime="text/plain; charset=utf-8",
    key="download_note",
)

with st.expander("↔ 비슷한 직업, 나란히 비교해 볼까요?"):
    comparison = st.multiselect(
        "비교할 직업을 2~3개 선택하세요",
        options=list(CAREERS),
        default=[selected, next(name for name in CAREERS if name != selected)],
        max_selections=3,
        key=f"compare_{selected}",
    )
    if len(comparison) < 2:
        st.info("직업을 두 개 이상 고르면 주요 차이를 볼 수 있어요.")
    else:
        for column, name in zip(st.columns(len(comparison)), comparison):
            other = CAREERS[name]
            with column:
                st.markdown(f"### {other['icon']} {name}")
                st.write(other["short"])
                st.markdown("**대표 질문**")
                st.write(other["question"])
                st.markdown("**핵심 도구 예시**")
                st.write(" · ".join(tool for tool, _ in other["stack"]["먼저 익히기"]))
                st.markdown("**대표 산출물**")
                st.write(other["case"]["deliverable"])

with st.expander("소개를 읽기 전에 · 직무 범위와 참고 자료"):
    st.write("이 페이지는 커리어 탐색을 위한 설명입니다. 회사·산업·경력 단계에 따라 직무 이름과 업무 범위가 달라집니다. 도구는 대표적인 예시이고, 실무 사례와 학습 순서는 이해를 돕기 위해 구성했습니다.")
    st.markdown("- [IBM · 데이터 과학의 개념](https://www.ibm.com/think/topics/data-science)\n- [IBM · MLOps와 모델 운영](https://www.ibm.com/think/topics/mlops)")

html('<footer>next track ♡ <span>취향을 발견하듯, 나의 일을 발견하기.</span><br><small>DATA & AI CAREER CLUB · an independent career guide</small></footer>')
