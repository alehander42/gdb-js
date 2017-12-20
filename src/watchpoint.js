class Watchpoint {
  /**
   * Create a watchpoint object
   * Usually you don't need to create it yourself unless
   * you're doing some low-level stuff
   *
   * @param {number} id The internal GDB ID of a watchpoint
   * @param {string} exp The expression
   * @param {object} [options] The options object
   */
  constructor (id, options = {}) {
    /**
     * The internal GDB ID of a watchpoint
     *
     * @type {number}
     */
    this.id = id

    /**
     * The expression
     *
     * @type {string}
     */
    this.exp = options.exp

    this.thread = options.thread || null
  }
}

export default Watchpoint
