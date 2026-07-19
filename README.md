<div align="center">

<img src="assets/banner-jabuti.jpg" width="100%" alt="Banner: um jabuti-piranga comendo folhas de couve" />

<img src="https://www.gravatar.com/avatar/1afa0bc66f32532d62ebac1f0f55adfa?s=280" width="150" alt="Foto de Matheus Antonio Vivas Rocha" />

# Matheus Antonio Vivas Rocha

<img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&size=20&pause=1000&color=1D9E75&center=true&vCenter=true&width=580&lines=Engenharia%20El%C3%A9trica%20%40%20EESC-USP%20%E2%9A%A1;Sistemas%20de%20Pot%C3%AAncia%20%26%20Simula%C3%A7%C3%A3o%20Computacional;Criador%20do%20pynatem%20%F0%9F%93%A6;Do%20fluxo%20de%20pot%C3%AAncia%20ao%20ESP32%20%F0%9F%94%8C" alt="Frases animadas sobre o perfil de Matheus Antonio Vivas Rocha" />

<!-- gravatar:links -->
[![LinkedIn](https://img.shields.io/badge/LinkedIn-matheusvivasr-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/matheusvivasr)
<!-- /gravatar:links -->
[![X](https://img.shields.io/badge/X-%40matheusvivasr-000000?style=flat&logo=x&logoColor=white)](https://twitter.com/matheusvivasr)
[![Email](https://img.shields.io/badge/email-vivas.matheus%40usp.br-blue?style=flat&logo=gmail&logoColor=white)](mailto:vivas.matheus@usp.br)
![Followers](https://img.shields.io/github/followers/matheusvivasr?label=followers&style=social)
![Profile views](https://komarev.com/ghpvc/?username=matheusvivasr&label=Profile%20views&color=1D9E75&style=flat)

📍 <!-- gravatar:location -->São Carlos - SP 🇧🇷<!-- /gravatar:location -->

</div>

---

### 👋 Sobre mim

**Engenharia Elétrica** na **EESC‑USP** (São Carlos), com foco em **sistemas de potência computacionais** — e uma queda por resolver problemas de **ponta a ponta**, do modelo matemático ao ferro que fica na parede.

Desenvolvo bibliotecas open‑source em Python que conversam com os principais simuladores do setor elétrico brasileiro — **ANAREDE** (fluxo de potência) e **ANATEM** (estabilidade eletromecânica transitória), ambos do CEPEL — e, nas horas vagas, levo o mesmo rigor para o **hardware** (ESP32) e para a **linguagem da HP Prime**.

- 🔭 `pynatem` publicado e estável no PyPI — a base do que faço em simulação
- 🔌 Do software ao ferro: firmware **ESP32** (ESP‑NOW, sensores capacitivos, SSR 220 V, deep sleep)
- 🧮 Entusiasta de **HP Prime** — fiz linter, extensão de VS Code e automação para a linguagem **PPL**
- 🐢 Até o abrigo de um **jabuti** virou projeto de ESP32 (controle térmico + *fail‑safe*)
- 🦈 Pull Shark no GitHub — PRs mesclados em outros projetos
- 💬 Fale comigo sobre **sistemas de potência, simulação, Python científico ou embarcados**

<table align="center"><tr><td align="center">
<img src="assets/jabuti.jpg" width="150" alt="O jabuti do Matheus" /><br>
<sub>🐢 o astro do projeto <a href="https://github.com/matheusvivasr/basking-spot"><code>basking-spot</code></a></sub>
</td></tr></table>

---

### 🚀 Projeto em destaque — `pynatem`

[![PyPI](https://img.shields.io/pypi/v/pynatem?color=blue&label=PyPI)](https://pypi.org/project/pynatem/)
[![License](https://img.shields.io/github/license/matheusvivasr/pynatem)](https://github.com/matheusvivasr/pynatem/blob/main/LICENSE)
[![Tests](https://img.shields.io/badge/tests-295%20passing-brightgreen)](https://github.com/matheusvivasr/pynatem)
[![Type hints](https://img.shields.io/badge/type%20hints-full-brightgreen)](https://github.com/matheusvivasr/pynatem)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/psf/black)

Biblioteca Python para **gerar, manipular e fazer parsing** de arquivos de caso (`.stb`) do **ANATEM/CEPEL** — o simulador de estabilidade eletromecânica transitória usado no setor elétrico brasileiro. Representa o `.stb` como um **grafo de blocos serializáveis** (padrão *AST + Serializer*): modela máquinas síncronas, reguladores de tensão/velocidade, PSS, FACTS, HVDC e OLTC, com *roundtrip* garantido e serialização fiel ao **Manual 12.10 do CEPEL** — validada seção a seção contra o manual oficial.

```bash
pip install pynatem
```

🔗 [github.com/matheusvivasr/pynatem](https://github.com/matheusvivasr/pynatem) &nbsp;·&nbsp; 📦 [pypi.org/project/pynatem](https://pypi.org/project/pynatem/)

---

### ⚡ Sistemas de Potência & Simulação

| Projeto | O que faz |
|---|---|
| 📦 **[pynatem](https://github.com/matheusvivasr/pynatem)** | Geração/parsing de casos `.stb` do **ANATEM** — *roundtrip* fiel ao Manual CEPEL (publicado no PyPI) |
| ⚡ **[newton-powerflux](https://github.com/matheusvivasr/newton-powerflux)** | Solver de **fluxo de potência** por Newton‑Raphson, compatível com arquivos padrão ANAREDE |

---

### 🔌 Hardware & Embarcados

| Projeto | O que faz |
|---|---|
| 💧 **[caixa-dagua](https://github.com/matheusvivasr/caixa-dagua)** | Medidor de **nível de caixa d'água sem contato** — dois nós **ESP32‑C3** (sensores capacitivos AT42QT1070 + **ESP‑NOW** + deep sleep; nó base serve o site em tempo real) |
| 🐢 **[basking-spot](https://github.com/matheusvivasr/basking-spot)** | Controle **térmico e de fotoperíodo** de um recinto de jabuti — **ESP32‑S3**, NTC10K, SSR 220 V, histerese e *fail‑safe* de segurança |

---

### 🧰 Ferramentas & DevTools

| Projeto | O que faz |
|---|---|
| 🧩 **[hp-prime-ppl](https://github.com/matheusvivasr/hp-prime-ppl)** | Extensão de **VS Code** para a linguagem **PPL** da HP Prime — realce, **linter**, autocompletar e hover (~700 comandos, análise estática de `.hpprgm`) |
| 🤖 **[hp-prime-automation](https://github.com/matheusvivasr/hp-prime-automation)** | Automação do **HP Connectivity Kit / Virtual Calculator** (pyautogui) com coordenadas relativas ao header da janela |
| 🔤 **[Conversor-de-Unidades](https://github.com/matheusvivasr/Conversor-de-Unidades)** | Conversor de unidades em Python, com interface gráfica **GTK+ / Glade** |
| 📚 **[SEL0456](https://github.com/matheusvivasr/SEL0456)** · **[CalcNum](https://github.com/matheusvivasr/CalcNum)** | Códigos e exercícios de disciplinas da EESC‑USP |

---

### 💻 Stack

![Python](https://img.shields.io/badge/Python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![C++](https://img.shields.io/badge/C++-00599C?style=flat&logo=cplusplus&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat&logo=typescript&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=flat&logo=nodedotjs&logoColor=white)
![ESP32](https://img.shields.io/badge/ESP32-E7352C?style=flat&logo=espressif&logoColor=white)
![PlatformIO](https://img.shields.io/badge/PlatformIO-FF7F00?style=flat&logo=platformio&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white)
![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=flat&logo=latex&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)

---

### 📊 GitHub stats

<div align="center">
<img height="165" src="https://github-readme-stats-flax-seven-17.vercel.app/api?username=matheusvivasr&show_icons=true&count_private=true&theme=tokyonight&hide_border=true" alt="Estatísticas do GitHub de matheusvivasr" />
<img height="165" src="https://github-readme-stats-flax-seven-17.vercel.app/api/top-langs/?username=matheusvivasr&layout=compact&theme=tokyonight&hide_border=true" alt="Linguagens mais usadas por matheusvivasr" />
</div>

<div align="center">
<img src="https://streak-stats.demolab.com/?user=matheusvivasr&theme=tokyonight&hide_border=true" alt="Streak de contribuições de matheusvivasr" />
</div>

---

<div align="center">
<sub>⚡ Do fluxo de potência ao ESP32 · Perfil repaginado em julho de 2026</sub>
</div>
