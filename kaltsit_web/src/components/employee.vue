<script>
export default {
  data () {
    return {
      employeeList: [],
      employeeParam: [],
      employeeMax: [],
      employeeMin: []
    }
  },
  created () {
    this.getEmployeeList()
  },
  methods: {
    getEmployeeList () {
      const employeeList = require('../static/employee_table_sim.json')
      this.employeeList = employeeList.char_285_medic2
      this.employeeMax = employeeList.phases.
    }
  }
}
</script>
