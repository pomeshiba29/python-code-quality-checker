# Python Code Quality Checker

Pythonコードの品質を自動で整えるシンプルなツールです。

以下のツールを組み合わせて、コード品質チェックを自動化します。

- ruff : コード問題の検出・自動修正
- black : コードフォーマット統一
- flake8 : コード品質チェック
- tox : 上記ツールの一括実行

---

# 処理フロー

Pythonコードを `check_codes` フォルダに配置し、toxを実行すると以下の処理が行われます。

```
check_codes
↓
ruff → black → flake8
↓
品質が整ったPythonコード`
```

---

# ディレクトリ構成

```
python-code-quality-checker/
│
├─ check_codes/                 # ここにチェックしたいPythonコードを配置
│   └─ ここにチェックしたいコードをいれてください.txt
│
├─ sample_bad_code/             # サンプル（品質の悪いコード例）
│   └─ test.py
│
├─ tox.ini                      # ruff / black / flake8 をまとめて実行する設定
├─ pyproject.toml               # black / ruff の設定
├─ requirements.txt             # 必要ライブラリ
└─ .gitignore                   # Git管理対象外ファイル
```

---

# 使い方

以下の手順でコード品質チェックを実行できます。

---

## 1. リポジトリをダウンロード

GitHubの「Code」→「Download ZIP」からダウンロードします。

ZIPファイルを解凍すると以下のフォルダが作成されます。

```
python-code-quality-checker/
```

---

## 2. フォルダに移動

コマンドプロンプトまたはターミナルで、解凍したフォルダへ移動します。

```bash
cd python-code-quality-checker
```

---

## 3. 仮想環境を作成

Pythonの仮想環境を作成します。

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Mac / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

---

## 4. 必要ライブラリをインストール

```bash
pip install -r requirements.txt
```

インストールされる主なツール

- ruff
- black
- flake8
- tox

---

## 5. チェックしたいPythonコードを配置

`check_codes` フォルダに対象コードを入れます。

例

```
check_codes/
    sample.py
```

※sample_bad_code のフォルダに入っている「test.py」ファイルを上記フォルダに移動することで動作チェックも行えます。

---

## 6. コード品質チェックを実行

以下のコマンドを実行します。

```bash
tox -e lint
```

---

## 実行される処理

`tox -e lint` を実行すると以下が順番に実行されます。

```
ruff → black → flake8
```

|ツール|処理内容|
|---|---|
ruff|コード問題の検出・自動修正|
black|コードフォーマット統一|
flake8|コード品質チェック|

---

## 実行イメージ

```
check_codes/
    sample.py
```

↓

```
tox -e lint
```

↓

```
ruff → black → flake8
```

↓

```
品質の整ったPythonコード
```

---
