




/*
  =====  Footer =====
*/

class footerSecion extends HTMLElement{
    connectedCallback(){
      this.innerHTML =`
      <section class="contact">
      <div class="text-box">
        <h1>Enroll For Our Various Online Courses
          <br>  Anywhere from the World</h1>
            <button class="btn"><a class="white"> Visit us to know more</a></button>
      </div>
    </section>
      <section class="about">
      <h2>About Us</h2>
      <p>OpenLabs (previously NIIT Ghana) is the most well-known name in West African IT education. We are best recognized for our training, consulting, and content production capabilities. OpenLabs offers a diverse selection of education programs that appeal to people from all walks of life, from businesses with growing training needs to individuals seeking IT and related skills. Our unrivaled knowledge, brand appeal, and constantly expanding global reach, all developed over 20 years, have made us a reliable education partner for students and professionals alike. We are proud of our strategic alliances with Microsoft, IBM, Google for Education, Huawei, ATHE, and other internationally renowned organizations. These affiliations demonstrate our trustworthiness and dedication to IT education. OpenLabs is now collaborating with BlueCrest University colleges in Liberia and Sierra Leone to provide academic training materials and consulting services to help them enhance their brand in vocational and skill development.</p>
      
          <h2>Contact Me</h2>
          <div class="social-icons">
          
          <a href="https://www.linkedin.com/in/raunak-sharma-72202822b"><img class="social-icon" src="./Photos/social-img/icons8-linkedin-2.gif" alt=""></a>
          
          <a href="https://github.com/Sharma572"><img class="social-icon"  src="./Photos/social-img/icons8-github.gif" alt=""></a>
          
          <a href="www.facebook.com"><img class="social-icon" src="./Photos/social-img/icons8-facebook-64.png" alt=""></a>
  
          <a href="www.gmail.com"><img class="social-icon" class="social-icon"  src="./Photos/social-img/icons8-gmail-48.png"alt=""></a>
  
          <a href="www.instagram.com"><img class="social-icon"  src="./Photos/social-img/icons8-instagram.gif"></a>
  
      </div>
      <h4 class="rights">All Rigths are Reserved By ❤️ StanDev@OpenLab</h4>
  </section>
      `
    }
  }
//   customElements.define('my-header', MyHeader);
  customElements.define("footer-section",footerSecion);
  
