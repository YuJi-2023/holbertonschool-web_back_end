export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
    if (this.constructor !== Building) {
      this.evacuationWarningMessage();
    }
  }

  get sqft() {
    return this._sqft;
  }

  evacuationWarningMessage() {
    this._sqft = this.sqft;
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
