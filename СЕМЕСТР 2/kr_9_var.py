import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from sklearn.linear_model import PassiveAggressiveRegressor
from scipy.stats import loguniform
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import mean_squared_log_error


np.random.seed(0)
x = np.linspace(0.1, 15, 100).reshape(-1, 1)
y_true = np.exp(0.3 * x[:, 0]) * np.cos(2 * x[:, 0]) + 50
noise = np.random.normal(0, 0.2, size=y_true.shape)
y_noisy = y_true + noise

param_dist = {
    'C': [0.1, 1, 10],
    'epsilon': [0.01, 0.1, 0.5],
    'loss': ['epsilon_insensitive']
}

base_model = PassiveAggressiveRegressor(max_iter=100, random_state=0)
search = RandomizedSearchCV(base_model, param_distributions=param_dist, n_iter=10,
                          scoring='neg_mean_squared_error', cv=3, random_state=0)
search.fit(x, y_noisy)
best_params = search.best_params_
print("Лучшие параметры:", best_params)


model = PassiveAggressiveRegressor(**best_params, max_iter=1, warm_start=True, random_state=0)
epochs = 50
predictions = []
msle_values = []

for epoch in range(epochs):
    model.partial_fit(x, y_noisy.ravel())
    y_pred = model.predict(x)
    predictions.append(y_pred.copy())
    
    y_pred_clipped = np.clip(y_pred, a_min=0.1, a_max=None)  
    y_true_clipped = np.clip(y_true, a_min=0.1, a_max=None)
    msle = mean_squared_log_error(y_true_clipped, y_pred_clipped)
    msle_values.append(msle)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), gridspec_kw={'height_ratios': [3, 1]})

ax1.plot(x, y_true, 'g-', label='Истинная функция')
ax1.scatter(x, y_noisy, color='gray', s=10, alpha=0.6, label='Шумные данные')
pred_line, = ax1.plot(x, predictions[0], 'r-', label='Предсказание')
ax1.set_title('Обучение PassiveAggressiveRegressor')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True)

msle_line, = ax2.plot(range(epochs), msle_values, 'b-', label='MSLE')
ax2.set_xlabel('Эпоха')
ax2.set_ylabel('MSLE')
ax2.legend()
ax2.grid(True)

ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
slider = Slider(ax_slider, 'Эпоха', 1, epochs, valinit=1, valstep=1)

def update(val):
    epoch = int(slider.val) - 1
    pred_line.set_ydata(predictions[epoch])
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.tight_layout()
plt.show()