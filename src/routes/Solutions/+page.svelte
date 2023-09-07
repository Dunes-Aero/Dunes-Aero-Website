<script>
	function move(){
	const productContainers = [...document.querySelectorAll('.product-container')];
const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
const preBtn = [...document.querySelectorAll('.pre-btn')];

productContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})
}
 </script>

<section>
	
	<div class="header">   
	
		<h1 class="xl:text-5xl lg:text-4xl text-2xl text-center text-secondary font-bold ">Dunes aero Solutions</h1>

	<h5 class="xl:text-5xl lg:text-4xl text-2xl text-center text-primary font-bold ">Tailoring the Sky to Your Needs. Beyond our specialized services and solutions, we offer bespoke drone solutions, innovatively designed to meet the unique demands of your business. </h5>

</div>


	<div class="product">
			
			<button class="pre-btn" on:click={move}><img src="src\lib\assets\images\arrow.png" alt=""></button>
			<button class="nxt-btn" on:click={move}><img src="src\lib\assets\images\arrow.png" alt=""></button>

			<div class="product-container">
					<div class="product-card">
							<img src="src\lib\assets\images\sol1.svg" class="product-thumb" alt="2">
					</div>
					<div class="product-card">
							<img src="src\lib\assets\images\sol2.svg" class="product-thumb" alt="3">
					</div>
					<div class="product-card">
							<img src="src\lib\assets\images\sol3.svg" class="product-thumb" alt="4">
					</div>
					<div class="product-card">
							<img src="src\lib\assets\images\sol4.svg" class="product-thumb" alt="5">
					</div>
					<div class="product-card">
							<img src="src\lib\assets\images\sol5.svg" class="product-thumb" alt="s5">
					</div>
					<div class="product-card">
							<img src="src\lib\assets\images\sol6.svg" class="product-thumb" alt="7">
					</div>
					<div class="product-card">
							<img src="src\lib\assets\images\sol7.svg" class="product-thumb" alt="">
					</div>
					<div class="product-card">
							<img src="src\lib\assets\images\sol8.svg" class="product-thumb" alt="">
					</div>
					<div class="product-card">
							<img src="src\lib\assets\images\sol9.svg" class="product-thumb" alt="">
					</div>
					<div class="product-card">
							<img src="src\lib\assets\images\sol10.svg" class="product-thumb" alt="">
					</div>
			</div>
	</div>

	<h6>Your vision, our flight - together.</h6>
</section>
	 
 

<style>
  
 
.header{
 
padding-top: 20px;
text-align: center;
	
} 
.title{
color: var(--color-secondary);
padding-bottom: 3%;
font-size: 30px;
}
.body{
color:var(--color-secondary); 
}

 section{
  background-color: #112B3C;
height:780px;

 } 

/* PRODUCTS */
.product {
  position: relative;
  overflow: hidden;
  padding: 20px;
  
}
 

.product-container {
  padding: 0 10vw;
  display: flex;
  overflow-x: auto;
  scroll-behavior: smooth;

}

.product-container::-webkit-scrollbar {
  display: none;
}

.product-card {
  flex: 0 0 auto;
  width: 250px;
  height: 250px;
  margin-right: 40px;
}

 

.product-thumb {

 
  width: 224px;
  height: 230px;
  object-fit: cover;
  
}

 
 

.product-card:hover .card-btn {
  opacity: 1;
}

.card-btn:hover {
  background: #ff7d7d;
  color: #fff;
}

 
 

 

.pre-btn,
.nxt-btn {
  border: none;
  width: 10vw;
  height: 100%;
  position: absolute;
  top: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, #fff 100%);
  cursor: pointer;
  z-index: 8;
}

.pre-btn {
  left: 0;
  transform: rotate(180deg);
}

.nxt-btn {
  right: 0;
}

.pre-btn img,
.nxt-btn img {
  opacity: 0.2;
}

.pre-btn:hover img,
.nxt-btn:hover img {
  opacity: 1;
}

.collection-container {
  width: 100%;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-gap: 10px;
}

.collection {
  position: relative;
}

.collection img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.collection p {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: #fff;
  font-size: 50px;
  text-transform: capitalize;
}

.collection:nth-child(3) {
  grid-column: span 2;
  margin-bottom: 10px;
}

</style>
