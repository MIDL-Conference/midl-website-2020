---
title: "DIVA: Domain Invariant Variational Autoencoder"
page_class: "paper"
---

{% from "_macros.html" import presentation, button, teaser, youtube %}

# O043 - DIVA: Domain Invariant Variational Autoencoder

### Maximilian Ilse, Jakub M. Tomczak, Christos Louizos, Max Welling

[% .details %]
<a class="toggle_visibility" data-selector=".abstract" data-level="3">Show abstract</a>
- <a class="toggle_visibility" data-selector=".schedule" data-level="3">Show schedule</a>
- <a href="https://openreview.net/pdf?id=RmNckVums7">Paper</a>
- <a href="https://openreview.net/forum?id=RmNckVums7">Reviews</a>
{{ teaser('pLSElJxW7vM') }}

<p>
    <span class="abstract">
        We consider the problem of domain generalization, namely, how to learn representations given data from a set of domains that generalize to data from a previously unseen domain. We propose the Domain Invariant Variational Autoencoder (DIVA), a generative model that tackles this problem by learning three independent latent subspaces, one for the domain, one for the class, and one for any residual variations. We highlight that due to the generative nature of our model we can also incorporate unlabeled data from known or previously unseen domains. To the best of our knowledge this has not been done before in a domain generalization setting. This property is highly desirable in fields like medical imaging where labeled data is scarce. We experimentally evaluate our model on the rotated MNIST benchmark and a malaria cell images dataset where we show that (i) the learned subspaces are indeed complementary to each other, (ii) we improve upon recent works on this task and (iii) incorporating unlabelled data can boost the performance even further.
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide abstract</a></span>
    </span>
</p>

<p>
    <span class="schedule">
        Oral Session #2 - Limited Data  - 12:30 - 13:30 UTC-4 (Monday)<br>Poster Session #2  - 13:30 - 15:00 UTC-4 (Monday)
        <br>
        <span class="actions"><a class="toggle_visibility" data-level="2">Hide schedule</a></span>
    </span>
</p>

{{ button("Access paper channel", "https://chat.midl.io/channel/o043") }}
[% / %]

---


### Oral presentation

---

{{ presentation('1GBSjGtr2rE', '/slides/ilse20.pdf', 720, 450) }}