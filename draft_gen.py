import re

def split_sentences(text):
  # ピリオドで文を区切る（ピリオドの後にスペースまたは改行が続く場合）
  sentences = re.split(r'\.\s+', text.strip())
  # 最後の文にピリオドが残っていなければ追加
  sentences = [s if s.endswith('.') else s + '.' for s in sentences if s]
  return sentences

def format_sentences(sentences):
  formatted = []
  for sentence in sentences:
    formatted.append(r"\newsentence")
    formatted.append(f"{{{sentence}}}")
    formatted.append("{}\n")
  return '\n'.join(formatted)

def main():
  with open("input.txt", "r", encoding="utf-8") as f:
    input_text = f.read()
  sentences = split_sentences(input_text)
  formatted_text = format_sentences(sentences)
  with open("output.txt", "w", encoding="utf-8") as f:
    f.write(formatted_text)

if __name__ == "__main__":
  main()