<script>
   export let icon=''
</script>



<div class="flex gap-5">
    <img src={icon} alt="contact-icon">
    <p class="text-lg"><slot/></p>
</div>