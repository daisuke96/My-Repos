<template>
  <div>
    <span>Memo</span><br>
    <textarea v-model="message" placeholder="memo" cols="60" rows="10"></textarea>

  </div>




</template>

<script>

export default {
  name: 'MemoList',
  data(){
    return{
      message: ''
    }
  }

}
</script>