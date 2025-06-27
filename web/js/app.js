import { app } from "../../../scripts/app.js";

app.registerExtension({
  name: "comfypsi.force.connect",

  async beforeRegisterNodeDef(nodeType) {
    const onNodeCreated = nodeType.prototype.onNodeCreated;

    nodeType.prototype.onNodeCreated = function () {
      onNodeCreated?.apply(this, arguments);

      if (nodeType.comfyClass == "comfypsi_force_connect") {
        this.size[0] = 225;
      }
    };
  },
});
