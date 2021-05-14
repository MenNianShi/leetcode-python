import tensorflow as tf

def mode_fn(input_features):
    user_features =tf.embedding_lookup(input_features,self.user_feature_column)
    item_features =tf.embedding_lookup(input_features,self.user_feature_column)

    user_output = tf.layers.dense(user_features,128)
    item_output = tf.layers.dense(item_features,128)

    out = tf.multiply(user_output, item_output)
    pred = tf.nn.sigmod(out)
    return pred

def mode_fn(input_features):
    inputs = tf.concat([input_features],-1)
    expert_outs = expert_net(inputs)
    task_outs = []
    task_preds= []

    for i in range(self.task_num):
        with tf.variable_scope('task_{}'.format(i)) :
            task_out = task_net(inputs,expert_outs)
            task_pred = tf.nn.sigmoid(task_out)
            task_outs.append(task_out)
            task_preds.append(task_pred)
    return task_preds

def expert_net(inputs):
    expert_outs = []
    for i in range(self.expert_num):
        expert = tf.layers.dense(inputs, [64],activation='relu',reuse=True)
        expert_outs.append(expert)
    return expert_outs
def task_net(inputs,expert_outs):
    gated_out = tf.layers.dense(inputs,[64],activation='relu',reuse=True)
    gated_out = tf.nn.sigmoid(gated_out)
    gated_out = tf.tile(tf.expand_dims(gated_out, axis=1),[1,self.expert_num,1])
    task_out = tf.multiply(expert_outs,gated_out)
    task_out = tf.reduce_sum(task_out,axis=1)
    return task_out






