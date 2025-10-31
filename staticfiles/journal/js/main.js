document.addEventListener('DOMContentLoaded', function(){
  // 1) random icon cho mỗi note và random rotation
  const icons = ['🐻','🐰','🦊','🦋','🌸','🌷','☀️','⭐','🍑','🌼'];
  document.querySelectorAll('.note').forEach(n => {
    const ico = n.querySelector('.note-ico');
    if(ico){
      ico.textContent = icons[Math.floor(Math.random()*icons.length)];
      // màu nhẹ cho vòng icon
      ico.style.background = `linear-gradient(135deg, rgba(255,255,255,0.98), rgba(255,250,250,0.95))`;
    }
    // random rotation
    const r = (Math.random()*6 - 3).toFixed(2); // -3..3 deg
    n.style.setProperty('--rot', r + 'deg');
  });

  // 2) leaf fall
  const leafWrap = document.getElementById('leaf-wrap');
  function makeLeaf(){
    const leaf = document.createElement('div');
    leaf.className = 'leaf';
    // style random
    const left = Math.random()*100;
    const dur = 8 + Math.random()*8;
    const size = 14 + Math.random()*24;
    leaf.style.left = left + 'vw';
    leaf.style.width = size + 'px';
    leaf.style.height = size + 'px';
    leaf.style.opacity = 0.7 - Math.random()*0.4;
    leaf.style.animation = `fall ${dur}s linear`;
    leafWrap.appendChild(leaf);
    // remove after animation
    setTimeout(()=> leaf.remove(), (dur+1)*1000);
  }
  // create css for leaf
  const s = document.createElement('style');
  s.innerHTML = `
    .leaf{
      position:fixed; top:-10vh; background: radial-gradient(circle at 30% 20%, #ffb6d6, #ffd7e6);
      border-radius: 50% 30% 50% 30%;
      transform: rotate(20deg);
      z-index:0;
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    @keyframes fall{
      0%{ transform: translateY(-10vh) rotate(0deg); opacity:0 }
      10%{ opacity:1 }
      100%{ transform: translateY(110vh) rotate(360deg); opacity:0.9 }
    }
  `;
  document.head.appendChild(s);
  // spawn leaves slowly
  setInterval(()=> {
    if(Math.random() < 0.7) makeLeaf();
  }, 800);

  // 3) music control
  const audio = document.getElementById('bg-audio');
  const btn = document.getElementById('music-toggle');
  let playing = false;
  btn.addEventListener('click', function(){
    if(!playing){
      audio.play();
      btn.textContent = '🔊';
      playing = true;
    } else {
      audio.pause();
      btn.textContent = '🔈';
      playing = false;
    }
  });
  // don't autoplay on load to avoid browser block
});
