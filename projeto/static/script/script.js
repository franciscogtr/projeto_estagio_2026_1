document.addEventListener("DOMContentLoaded", () => {

  const botaoMobile = document.getElementById('mobile_btn');
  const botaoMobileX = document.getElementById('mobile_x');
  const menuMobile = document.getElementById('mobile_menu');

  const home = document.getElementById('home');
  const servicos = document.getElementById('sobre-container');
  const sobre = document.getElementById('contato-container');

  // Estado inicial
  menuMobile.style.display = 'none';
  botaoMobileX.style.display = 'none';

  // Abrir menu mobile
  botaoMobile.addEventListener('click', () => {
    menuMobile.style.display = 'block';
    botaoMobileX.style.display = 'block';
    botaoMobile.style.display = 'none';
  });

  // Fechar menu mobile
  botaoMobileX.addEventListener('click', () => {
    menuMobile.style.display = 'none';
    botaoMobileX.style.display = 'none';
    botaoMobile.style.display = 'block';
  });

  // Links desktop
  document.getElementById('link_home').addEventListener('click', () => {
    home.scrollIntoView({ behavior: 'smooth' });
  });

  document.getElementById('link_sobre').addEventListener('click', () => {
    servicos.scrollIntoView({ behavior: 'smooth' });
  });

  document.getElementById('link_contato').addEventListener('click', () => {
    sobre.scrollIntoView({ behavior: 'smooth' });
  });

  // Links mobile
  document.getElementById('mobile_link_home').addEventListener('click', () => {
    home.scrollIntoView({ behavior: 'smooth' });
    fecharMenuMobile();
  });

  document.getElementById('mobile_link_servicos').addEventListener('click', () => {
    servicos.scrollIntoView({ behavior: 'smooth' });
    fecharMenuMobile();
  });

  document.getElementById('mobile_link_sobre').addEventListener('click', () => {
    sobre.scrollIntoView({ behavior: 'smooth' });
    fecharMenuMobile();
  });

  document.getElementById('mobile-btn-menu').addEventListener('click', () => {
    sobre.scrollIntoView({ behavior: 'smooth' });
    fecharMenuMobile();
  });

  function fecharMenuMobile() {
    menuMobile.style.display = 'none';
    botaoMobileX.style.display = 'none';
    botaoMobile.style.display = 'block';
  }

});
