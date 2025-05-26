/*
--------------- Campus Html Component---------------------
*/

class campusSection extends HTMLElement{
    connectedCallback(){
        this.innerHTML = `
        <section class="campus">
        <h2>Our Global Campus</h2>
        <p>The University of Hartford's main campus is located on Bloomfield Avenue. Surrounded by green space, the main campus is divided into residential and academic buildings connected by a bridge that overlooks the north branch of the Park River, known to us as Hog River.</p>
        <!-- campus-Card -->
        <div class="campus-card grid-col-3">
            <div class="img camcard1">
                <img src="./Photos/images4.jpg" alt="nt" >
                <div class="layer">
                    <h3>ACCRA</h3>
                </div>
            </div>
            <div class="img camcard2" >
                <img src="./Photos/images11.jpg" alt="">
                <div class="layer">
                    <h3>KUMASI</h3>
                </div>
            </div>
            <div class="img camcard3">
                <img src="./Photos/washington.png" alt="">
                <div class="layer">
                    <h3>TAKWARADE</h3>
                </div>
            </div>
        </div>
     </section>
        `
    }
}
customElements.define("campus-section",campusSection);