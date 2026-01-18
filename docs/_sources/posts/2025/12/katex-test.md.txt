---
blogpost: true
date: 2025-12-16
tags: test
language: English
---

# Sphinxにおける数式のテスト

Sphinxにおける数式がちゃんと機能しているかのテスト．
以下はなんとなく書いたカルバック・ライブラー発散（KL発散）の式．

$$D_{KL}(P||Q)=\sum_{x\in X}P(x)\log\frac{P(x)}{Q(x)}$$

- $P,\,Q$ は「同じ確率空間上の離散確率分布」．$D_{KL}(P||Q)$ と
  $D_{KL}(Q||P)$
  が異なる値をとるので、類似度でありながらも「距離」とは言わない．
