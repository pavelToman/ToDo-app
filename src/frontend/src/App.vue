<script setup>
import axios from "axios";
import { ref, onMounted, computed } from "vue";
import Datepicker from "@vuepic/vue-datepicker";
import "@vuepic/vue-datepicker/dist/main.css";

let lists = ref([]);
let newList = ref("");
let notes = ref([]);
let newNoteText = ref("");
let selectedList = ref("");
let notesOfList = computed(() => {
  return notes.value.filter((note) => note.list === selectedList.value);
});
let showAddListBut = ref(false);
let showAddNoteBut = ref(false);
let showEditListBut = ref(false);
let newListName = ref("");
let showEditNote = ref(false);
let newDateTime = ref(new Date());

function loadLists() {
  axios.get("http://localhost:8000/lists/").then((response) => {
    lists.value = response.data;
    // console.log(lists.value);
  });
}
function addList() {
  axios
    .post("http://localhost:8000/lists/", { name: newList.value })
    .then((response) => {
      lists.value.push(response.data);
    });
  newList.value = "";
  showAddListBut.value = false;
}
function loadNotes() {
  axios.get("http://localhost:8000/notes/").then((response) => {
    notes.value = response.data;
  });
}
function addNote() {
  axios
    .post("http://localhost:8000/notes/", {
      text: newNoteText.value,
      list: selectedList.value,
      due_date: newDateTime.value,
    })
    .then((response) => {
      notes.value.push(response.data);
    });
  newNoteText.value = "";
  showAddNoteBut.value = false;
}
function setList(url) {
  selectedList.value = url;
  showAddListBut.value = false;
  showAddNoteBut.value = false;
  showEditNote.value = false;
  showEditListBut.value = false;
}
function showAddList() {
  showAddListBut.value = !showAddListBut.value;
}
function showAddNote() {
  showAddNoteBut.value = !showAddNoteBut.value;
}
function showEditList() {
  showEditListBut.value = !showEditListBut.value;
}
onMounted(() => {
  loadLists();
  loadNotes();
});
function newDone(note) {
  // console.log(note);
  axios.patch(note.url, { done: note.done });
}
function deleteNote(note) {
  axios.delete(note.url);
  notes.value = notes.value.filter((x) => x.url !== note.url);
}
function deleteList(list) {
  // console.log(list);
  axios.delete(list);
  loadLists();
  loadNotes();
}
function editList() {
  // console.log(selectedList.value);
  // console.log(newListName.value);
  axios.patch(selectedList.value, { name: newListName.value });
  loadLists();
  loadNotes();
}
function editNote(note) {
  axios.patch(note.url, { text: note.text }).then((response) => {
    note.push(response.data);
  });
  showEditNote.value = false;
}
function formatDate(date) {
  const datum = new Date(date);
  return new Intl.DateTimeFormat("default", {
    dateStyle: "short",
    timeStyle: "short",
  }).format(datum);
}
</script>

<template>
  <body class="grid">
    <div class="row p-3 bg-dark text-white">
      <div class="col">
        <h1><a href="/">To Do</a></h1>
      </div>
    </div>

    <div class="row pt-2">
      <ul class="nav nav-tabs">
        <li class="nav-item" v-for="list in lists" :key="list.url">
          <a
            class="nav-link"
            data-bs-toggle="tab"
            href="#"
            @click="setList(list.url)"
          >
            {{ list.name }}
          </a>
        </li>
        <li class="nav-item">
          <button
            class="nav-link"
            id="newList"
            v-if="!showAddListBut"
            @click="showAddList"
          >
            Add List
          </button>
          <form v-if="showAddListBut" @submit.prevent="addList">
            <input
              type="text"
              v-model="newList"
              placeholder="List name"
              autofocus
            />
            <button id="newList" class="btn btn-dark">Add List</button>
          </form>
        </li>
      </ul>
    </div>

    <div class="row pt-2 pb-2">
      <div class="btn-group">
        <button
          class="btn btn-primary"
          v-if="selectedList && !showAddNoteBut && !showEditListBut"
          @click="showEditList"
        >
          Edit List
        </button>
        <form
          v-if="selectedList && showEditListBut"
          @submit.prevent="editList()"
        >
          <input
            type="text"
            class="form-control"
            v-model="newListName"
            placeholder="List name"
            autofocus
          />
          <button id="newList" class="btn btn-dark">Edit List</button>
        </form>
        <button
          class="btn btn-primary"
          v-if="selectedList && !showAddNoteBut && !showEditListBut"
          @click="deleteList(selectedList)"
        >
          Delete List
        </button>
      </div>
      <div
        class="btn-group pt-2"
        role="group"
        aria-label="Basic outlined example"
      >
        <button
          class="btn btn-outline-primary"
          v-if="selectedList && !showAddNoteBut"
          @click="showAddNote"
        >
          Add Note
        </button>
        <form v-if="selectedList && showAddNoteBut" @submit.prevent="addNote">
          <input
            type="text"
            class="form-control"
            v-model="newNoteText"
            placeholder="Note text"
            autofocus
          />
          <Datepicker v-model="newDateTime" />
          <button id="newList" class="btn btn-dark">Add Note</button>
        </form>
        <button
          class="btn btn-outline-primary"
          v-if="selectedList && !showAddNoteBut"
          @click="showEditNote = !showEditNote"
        >
          {{ showEditNote ? "Notes Edit Done" : "Edit Notes" }}
        </button>
      </div>
    </div>
    <div class="row pt-2 pb-2">
      <div class="col">
        <ul class="list-inline">
          <li
            class="list-inline-item"
            v-for="note in notesOfList"
            :key="note.url"
          >
            <button
              v-if="showEditNote"
              class="btn btn-outline-primary btn-sm"
              @click="deleteNote(note)"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="16"
                height="16"
                fill="currentColor"
                class="bi bi-trash"
                viewBox="0 0 16 16"
              >
                <path
                  d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"
                />
                <path
                  fill-rule="evenodd"
                  d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"
                />
              </svg>
            </button>
            <form v-if="showEditNote" @submit.prevent="editNote(note)">
              <input
                type="text"
                class="form-control"
                v-model="note.text"
                placeholder="Note text"
              />
              <Datepicker v-model="note.due_date" />
              <button id="newList" class="btn btn-dark">Edit Note</button>
            </form>
            <div class="form-check">
              <input
                class="form-check-input"
                type="checkbox"
                v-model="note.done"
                @change="newDone(note)"
                :id="note.url"
              />
              <label class="form-check-label" :for="note.url">
                <span :class="{ done: note.done }">
                  {{ note.text }}
                </span>
                <p>
                  {{ note.due_date ? formatDate(note.due_date) : "" }}
                </p>
              </label>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </body>
</template>

<style scoped>
.done {
  text-decoration: line-through;
}

.nav-tabs .nav-item .nav-link:hover {
  background-color: #0d6efd;
  color: #ffffff;
}
.nav-tabs .nav-item .nav-link.active {
  background-color: #0d6efd;
  color: #ffffff;
}
#newList {
  background-color: #000000;
  color: #ffffff;
  margin-left: 3px;
}
#newList:hover {
  background-color: #000000;
  color: #1eff00;
}
.btn-group {
  display: inline;
}
.list-inline-item {
  border-left: 5px solid #0d6efd;
  padding: 5px;
  margin: 10px;
  background-color: #0d6dfd1c;
}
</style>
