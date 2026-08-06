/* =========================================================================
   Caliora Dubai — animation engine
   GSAP + ScrollTrigger (CDN). Expo easing, quiet & premium.
   Systems: nav compact, hero choreography, masked text reveals, scroll
   reveals w/ stagger, image parallax, counters, accordions, marquee.
   ========================================================================= */

document.documentElement.classList.remove("no-js");

gsap.registerPlugin(ScrollTrigger);
const EASE = "expo.out";
const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/* ---------- Nav: compact on scroll + mobile menu ---------- */
const nav = document.querySelector(".nav");
if (nav) {
  const onScroll = () => nav.classList.toggle("is-scrolled", window.scrollY > 24);
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  const burger = nav.querySelector(".nav__burger");
  const links = nav.querySelector(".nav__links");
  if (burger && links) {
    burger.addEventListener("click", () => links.classList.toggle("is-open"));
    links.querySelectorAll("a").forEach(a => a.addEventListener("click", () => links.classList.remove("is-open")));
  }
}

if (!reduced) {

  /* ---------- Hero load choreography ---------- */
  const hero = document.querySelector("[data-hero]");
  if (hero) {
    const tl = gsap.timeline({ defaults: { ease: EASE } });
    tl.fromTo(hero.querySelector(".hero-slide__bg"),
        { scale: 1.12 }, { scale: 1, duration: 1.8 }, 0)
      .fromTo(hero.querySelectorAll("[data-hero-line] > *"),
        { yPercent: 110 }, { yPercent: 0, duration: 1.1, stagger: 0.09 }, 0.15)
      .fromTo(hero.querySelectorAll("[data-hero-fade]"),
        { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.9, stagger: 0.08 }, 0.55)
      .fromTo(".nav",
        { y: -16, opacity: 0 }, { y: 0, opacity: 1, duration: 0.8 }, 0.4);
  }

  /* ---------- Masked line reveals (scroll) ---------- */
  document.querySelectorAll("[data-reveal-mask]").forEach(el => {
    gsap.to(el.children, {
      yPercent: -0, y: 0, transform: "translateY(0%)",
      duration: 1.1, ease: EASE, stagger: 0.08,
      scrollTrigger: { trigger: el, start: "top 85%" }
    });
  });

  /* ---------- Generic scroll reveals ---------- */
  gsap.utils.toArray("[data-reveal]").forEach(el => {
    gsap.to(el, {
      opacity: 1, y: 0, duration: 1.0, ease: EASE,
      delay: parseFloat(el.dataset.delay || 0),
      scrollTrigger: { trigger: el, start: "top 88%" }
    });
  });

  /* ---------- Staggered groups (cards, grids) ---------- */
  gsap.utils.toArray("[data-stagger]").forEach(group => {
    gsap.fromTo(group.children,
      { opacity: 0, y: 36 },
      {
        opacity: 1, y: 0, duration: 0.9, ease: EASE, stagger: 0.08,
        scrollTrigger: { trigger: group, start: "top 85%" }
      });
  });

  /* ---------- Parallax covers ---------- */
  gsap.utils.toArray("[data-parallax]").forEach(el => {
    gsap.fromTo(el, { yPercent: -8 }, {
      yPercent: 8, ease: "none",
      scrollTrigger: { trigger: el.parentElement, start: "top bottom", end: "bottom top", scrub: true }
    });
  });

  /* ---------- Number counters ---------- */
  gsap.utils.toArray("[data-count]").forEach(el => {
    const raw = el.dataset.count;
    const suffix = el.dataset.suffix || "";
    const target = parseFloat(raw);
    const obj = { v: 0 };
    gsap.to(obj, {
      v: target, duration: 1.6, ease: "expo.out",
      scrollTrigger: { trigger: el, start: "top 88%" },
      onUpdate: () => { el.textContent = Math.round(obj.v) + suffix; }
    });
  });

  /* ---------- Marquee ticker ---------- */
  document.querySelectorAll(".marquee").forEach(m => {
    const track = m.querySelector(".marquee__track");
    if (!track) return;
    track.innerHTML += track.innerHTML; // duplicate for seamless loop
    const width = track.scrollWidth / 2;
    const tween = gsap.to(track, { x: -width, duration: width / 60, ease: "none", repeat: -1 });
    m.addEventListener("mouseenter", () => gsap.to(tween, { timeScale: 0.35, duration: 0.6 }));
    m.addEventListener("mouseleave", () => gsap.to(tween, { timeScale: 1, duration: 0.6 }));
  });

} else {
  // Reduced motion: show everything, no counters animation
  document.querySelectorAll("[data-count]").forEach(el => {
    el.textContent = el.dataset.count + (el.dataset.suffix || "");
  });
}

/* ---------- Accordions (always functional) ---------- */
document.querySelectorAll(".accordion__item").forEach(item => {
  const toggle = item.querySelector(".accordion__toggle");
  const panel = item.querySelector(".accordion__panel");
  if (!toggle || !panel) return;
  toggle.addEventListener("click", () => {
    const isOpen = item.classList.contains("is-open");
    // close siblings
    item.parentElement.querySelectorAll(".accordion__item.is-open").forEach(sib => {
      if (sib === item) return;
      sib.classList.remove("is-open");
      gsap.to(sib.querySelector(".accordion__panel"), { height: 0, duration: 0.55, ease: EASE });
    });
    item.classList.toggle("is-open", !isOpen);
    gsap.to(panel, { height: isOpen ? 0 : "auto", duration: 0.65, ease: EASE });
  });
});

/* Open first accordion by default */
document.querySelectorAll("[data-accordion-open-first]").forEach(list => {
  const first = list.querySelector(".accordion__item");
  if (first) {
    first.classList.add("is-open");
    const p = first.querySelector(".accordion__panel");
    if (p) gsap.set(p, { height: "auto" });
  }
});

/* ---------- Footer year ---------- */
document.querySelectorAll("[data-year]").forEach(el => el.textContent = new Date().getFullYear());
