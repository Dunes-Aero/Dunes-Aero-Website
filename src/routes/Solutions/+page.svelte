<!-- !solve the solution problem *we want the images to be responsive* -->
<!-- !finish the functunality of the slider indicator *circle* -->
<script>
  import Carousel from 'svelte-carousel';
	import ResizeObserver from 'resize-observer-polyfill';
	import { onMount } from 'svelte';
	import { browser } from '$app/environment';

  let boxEl;
	let boxWidth;
	// Add the observer when component mounts and cleanup after
	onMount(() => {
		const resizeObserver = new ResizeObserver((entries) => {
			// We're only watching one element
			const entry = entries.at(0);

			//Get the block size
			boxWidth = entry.contentBoxSize[0].blockSize;
		});

		resizeObserver.observe(boxEl);

		// This callback cleans up the observer
		return () => resizeObserver.unobserve(boxEl);
	});

// 	function move(){
// 	const productContainers = [...document.querySelectorAll('.product-container')];
// const nxtBtn = [...document.querySelectorAll('.nxt-btn')];
// const preBtn = [...document.querySelectorAll('.pre-btn')];

// productContainers.forEach((item, i) => {
//     let containerDimensions = item.getBoundingClientRect();
//     let containerWidth = containerDimensions.width ;

//     nxtBtn[i].addEventListener('click', () => {
//         item.scrollLeft += containerWidth;
//     })

//     preBtn[i].addEventListener('click', () => {
//         item.scrollLeft -= containerWidth;
//     })
// })
// }

// let activeSlide = 0; // Initialize the active slide
//   let indicators = [0, 1, 2]; // Number of slides

  


 </script>

<section id = "solutions" class="bg-primary h-screen">
	
	<div class="header bg-primary">   
	
		<h1 class="xl:text-5xl lg:text-4xl text-2xl text-center text-secondary font-bold my-10">Dunes aero Solutions</h1>

    <h5 class="xl:text-3xl lg:text-2xl text-2xl text-center text-secondary font-bold py-12 w-3/4 mx-auto">Tailoring the Sky to Your Needs. Beyond our specialized services and solutions, we offer bespoke drone solutions, innovatively designed to meet the unique demands of your business.</h5>

</div>


<div class=" bg-primary ">
  <!-- <button class="pre-btn bg-primary-hover hover:bg-secondary-hover rounded" on:click={move}
  on:click={() => move('prev')}>
    
    <img src="src\lib\assets\images\right.svg" alt="">
  </button>
  <button class="nxt-btn bg-primary-hover hover:bg-secondary-hover rounded" on:click={move}
  on:click={() => move('next')}>
    
    <img src="src\lib\assets\images\right.svg" alt="">
  </button> -->
  {#if browser}
  <div class=" bg-primary">
    <Carousel
    particlesToShow={5}
    particlesToScroll={2}
  >
 
     
      <img src="src\lib\assets\images\sol1.svg" class="product-thumb" alt="2">
     
     
      <img src="src\lib\assets\images\sol2.svg" class="product-thumb" alt="3">
     
     
      <img src="src\lib\assets\images\sol3.svg" class="product-thumb" alt="4">
     
   
      <img src="src\lib\assets\images\sol4.svg" class="product-thumb" alt="5">
    
 

  
      <img src="src\lib\assets\images\sol5.svg" class="product-thumb" alt="s5">
     
     
      <img src="src\lib\assets\images\sol6.svg" class="product-thumb" alt="7">
     
     
      <img src="src\lib\assets\images\sol7.svg" class="product-thumb" alt="">
     
     
      <img src="src\lib\assets\images\sol8.svg" class="product-thumb" alt="">
     
 
  
      <img src="src\lib\assets\images\sol9.svg" class="product-thumb" alt="">
     
     
      <img src="src\lib\assets\images\sol10.svg" class="product-thumb" alt="">
     
  
</Carousel>
</div>

{/if}
<!-- 
  <div class="indicator-container flex justify-center mt-4">
    {#each indicators as indicator, index}
      <span
        class="indicator-dot rounded-full h-2 w-2 mx-2 bg-gray-400"
        class:selected={index === activeSlide}
      ></span>
    {/each}
  </div> -->
</div>

	<h6 class="xl:text-2xl lg:text-2xl text-1xl text-center text-secondary font-semibold my-10">Your vision, our flight - together.</h6>



  <!-- <script>
    // --------------------------

let activeSlide = 0; // Initialize the active slide
  let indicators = [0, 1, 2]; // Number of slides

  function move(direction) {
    if (direction === 'next') {
      if (activeSlide < indicators.length - 1) {
        activeSlide++;
      } else {
        activeSlide = 0; // Wrap to the first slide if at the end
      }
    } else {
      if (activeSlide > 0) {
        activeSlide--;
      } else {
        activeSlide = indicators.length - 1; // Wrap to the last slide if at the beginning
      }
    }
  }


  
  </script> -->
</section>
	 
 

<style>
    /* Indicator dot style */
    .indicator-dot {
    width: 8px;
    height: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease-in-out;
  }

  .indicator-dot.selected {
    background-color: #007bff; /* Change to your desired color */
  }
 
.header{
 
padding-top: 20px;
text-align: center;
	
} 
/* .title{
color: var(--color-secondary);
padding-bottom: 3%;
font-size: 30px;
} */
/* .body{
color:var(--color-secondary); 
} */

 /* section{
 background-color: #112B3C; 
height:780px; this will keep the scroling bar showing on the left so we will use h-screen on the 

 }  */

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
  /* this will change the spaces between the solutions */
}

 

.product-thumb {

  
}

 
 

/* .product-card:hover .card-btn {
  opacity: 1;
}

.card-btn:hover {
  background: #ff7d7d;
  color: #fff;
} */

 
 

 

.pre-btn,
.nxt-btn {
  border: none;
  width: 5vw;
  height: 100%;
  position: absolute;
  top: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  /* background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, #fff 100%); */
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
/* 
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
} */

</style>
