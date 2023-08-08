<script type="ts">

</script>


<table id="ReimageTable">
    <thead>
        <tr>
            <th> </th>
            <th>&nbsp;Subject</th>
            <th>&nbsp;Step</th>
            <th>&nbsp;Date Created</th>
            <th>&nbsp;Assigned To</th>
        </tr>
    </thead>

    <tbody>
        <tr>
            <td><input type="checkbox" name="check" value="check"></td>
            <td>#INC-[NUM]</td>
            <td>
                <select name="tasks-[NUM]">
                    <option value="Label">Label</option>
                    <option value="Decrypt">Decrypt</option>
                </select>
            </td>
            <td>01/01/2021</td>
            <td>John Doe</td>
    </tbody>
</table>


<style>

table {
  visibility: visible;
  border-collapse: collapse;
  width: 90%;
  margin-left: 10%;
  margin-top: 3%;
  font-size: 16px;
  font-family: GhandiSans, sans-serif;
}

table th:first-child {
  border-radius: 10px 0 0 10px;
  border-right: solid #cfd7df 3px;
}

table th:last-child{
  border-right: none;
}

thead {
  background: #ebeff3;
  text-align: left;
}

th {
  position: sticky;
  border-right: solid #cfd7df 2px;
}

tbody tr:hover {
  background-color: #f2f7fc;
}

tr td:first-child{
    border-right: solid #cfd7df 3px;
}

tbody tr{
  border-bottom: solid #ebeff3 .5px;
}

select {
  border-color: white;
  background-color: white;
  box-shadow: 0 0 0 0 white;
  text-align: left;
}
</style>