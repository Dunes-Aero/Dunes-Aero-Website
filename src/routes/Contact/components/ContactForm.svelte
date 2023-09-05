<script>
    import InputField from "$lib/components/InputField.svelte";
	import Button from "$lib/components/Button.svelte";
</script>

<div class="form-container  h-[660px] w-1/2 bg-primary border-secondary border-2 p-5 grid items-center">

    <form class='w-3/5'>
        <div class="flex justify-between">
            <InputField placeholder='First name' name='first-name' type='text' mode={true}>First Name</InputField>

            <InputField placeholder='Last name' name='last-name' type='text' mode={true}>Last Name</InputField>
        </div>

  <InputField placeholder='example@gmail.com' name='email' type='text' mode={true}>Email</InputField>
  <InputField placeholder='Inquiry' name='first-name' type='text' mode={true}>Select Subject</InputField>
  <InputField placeholder='Write your message' name='first-name' type='text' mode={true}>Message</InputField>


<div class="flex justify-center">  <Button type='submit' color='secondary'>Send Message</Button></div>

    </form>
</div>