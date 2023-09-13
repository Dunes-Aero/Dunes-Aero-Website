<script>
	import Title from '../About/components/title.svelte';
	import Desc from './components/processDescription.svelte';
	import Line from './components/line.svelte';
	import Item from './components/item.svelte';
</script>

<!-- <section
    id="process"
    class="container our-process relative w-full pb-16 mx-auto bg-hero bg-no-repeat bg-cover bg-center items-center"
>
    <div class="lg:p-6 p-10">
        <Title pageTitle="Order Process" elementHTML="h1" textColor="secondary" class="lg:w-full" />
    </div>

    <div>
        <Desc />
    </div>

    <div class="grid grid-cols-3 grid-rows-4 lg:pt-6 2xl:pt-16 w-full">

        <div class="row-span-4 col-span-1 flex flex-col items-center justify-center">
            <Item class="" textItems={['Understanding your', ' business needs']} iconName="business" />
            <Item class="" textItems={['Order fulfilling and', 'support']} iconName="support" />
        </div>
        
        <div class="col-span-1 row-span-4 flex flex-col justify-center items-center">
            <Line />
        </div>
        

        <div class="row-span-4 col-span-1 flex flex-col items-center justify-center">
            <Item isRightLeft="yes" class="mb-1" textItems={['Contact Us']} iconName="contact" />
            <Item isRightLeft="yes" class="mb-1" textItems={['Finalize your order']} iconName="order" />
        </div>
    </div>
</section> -->

<!-- <section
	id="process"
	class="container our-process relative w-full pb-16 mx-auto bg-hero bg-no-repeat bg-cover bg-center items-center"
>
	<div class="lg:p-6 p-10">
		<Title pageTitle="Order Process" elementHTML="h1" textColor="secondary" class="lg:w-full" />
	</div>

	<div>
		<Desc />
	</div>

	<div class="flex justify-center items-center">

		<div class="flex flex-col items-center justify-start lg-screen">
			<div class="item-one relative">
				<Item textItems={['Understanding your', ' business needs']} iconName="business" />
			</div>
			<div class="item-two relative">
				<Item textItems={['Order fulfilling and', 'support']} iconName="support" />
			</div>
		</div>


		<div class="flex flex-col justify-center items-center p-12">
			<Line />
		</div>

		<div class="flex flex-col items-center justify-center lg-screen">
			<div class="item-three relative">
				<Item isRightLeft="yes" textItems={['Contact Us']} iconName="contact" />
			</div>
			<div class="item-fourth relative">
				<Item isRightLeft="yes" textItems={['Finalize your order']} iconName="order" />
			</div>
		</div>
	</div>
</section> -->
<section
	id="process"
	class="container our-process relative w-full pb-16 mx-auto bg-hero bg-no-repeat bg-cover bg-center items-center"
>
	<div class="lg:p-6 p-10">
		<Title pageTitle="Order Process" elementHTML="h1" textColor="secondary" class="lg:w-full" />
	</div>

	<div>
		<Desc />
	</div>

	<div class="flex justify-center items-center">
		<div class="flex flex-col items-center justify-start lg-screen">
			<div class="item-one relative">
				<Item
					titleContent="Understanding your business needs"
					textContent="Our team will collaborate with you to gather information about your specific requirements, use case, challenges, and objectives, preparing a comprehensive presentation showcasing recommended drone solutions."
					textItems={['Understanding your', ' business needs']}
					iconName="business"
				/>
			</div>
			<div class="item-two relative">
				<Item
					titleContent="Order fulfilling and support"
					textContent="After finalizing the order, our team will handle hardware development, procurement, assembly, installation, software configuration, training programs, and technical support to ensure your drone solution success."
					textItems={['Order fulfilling and', 'support']}
					iconName="support"
				/>
			</div>
		</div>

		<div class="flex flex-col justify-center items-center p-12">
			<Line />
		</div>

		<div class="flex flex-col items-center justify-center lg-screen">
			<div class="item-three relative">
				<Item
					titleContent="Contact Us"
					textContent="get in touch with our team. You can reach us at
				any time. we are ready to assist you and answer
				any initial inquiries you may have.
				"
					isRightLeft="yes"
					textItems={['Contact Us']}
					iconName="contact"
				/>
			</div>
			<div class="item-fourth relative">
				<Item
					titleContent="Finalize your order"
					textContent="After reviewing the presented solutions, we will prepare a detailed proposal outlining recommended products, services, and pricing structure, and after your acceptance, finalize the order."
					isRightLeft="yes"
					textItems={['Finalize your order']}
					iconName="order"
				/>
			</div>
		</div>
	</div>
</section>

<!-- <section
	id="process"
	class="container our-process relative w-full pb-16 mx-auto bg-hero bg-no-repeat bg-cover bg-center items-center"
>
	<div class="lg:p-6 p-10">
		<Title pageTitle="Order Process" elementHTML="h1" textColor="secondary" class="lg:w-full" />
	</div>

	<div>
		<Desc />
	</div>

	<div class="grid-container justify-center items-center">
		<div class="item1 flex flex-col items-center justify-start lg-screen">
			<div class="item-one relative">
				<Item textItems={['Understanding your', ' business needs']} iconName="business" />
			</div>
			<div class="item-two relative">
				<Item textItems={['Order fulfilling and', 'support']} iconName="support" />
			</div>
		</div>

		<div class="flex flex-col justify-center items-center p-12">
			<Line />
		</div>

		<div class="item2 flex flex-col items-center justify-center lg-screen">
			<div class="item-three relative">
				<Item isRightLeft="yes" textItems={['Contact Us']} iconName="contact" />
			</div>
			<div class="item-fourth relative">
				<Item isRightLeft="yes" textItems={['Finalize your order']} iconName="order" />
			</div>
		</div>
	</div>
</section> -->

<style>
	@import '../About/global.css';

	.our-process {
		background-color: var(--color-primary);
	}
	.item-one {
		top: -32px;
	}
	.item-two {
		top: 145px;
	}
	.item-three {
		top: -145px;
	}
	.item-fourth {
		top: 14px;
	}
	/* @media (max-width: 480px) {
		.item-one {
			top: -30px;
		}
		.item-two {
			top: 120px;
		}
		.item-three {
			top: -130px;
		}
		.item-fourth {
			top: 22px;
		}
	} */
	@media (max-width: 768px) {
		.item-one {
			top: -10px;
		}
		.item-two {
			top: 90px;
		}
		.item-three {
			top: -90px;
		}
		.item-fourth {
			top: 17px;
		}
	}
	@media (min-width: 1300px) {
		.lg-screen {
			padding: 80px;
		}
		.item-one {
			top: -46px;
		}
		.item-two {
			top: 186px;
		}
		.item-three {
			top: -190px;
		}
		.item-fourth {
			top: 22px;
		}
	}
</style>
